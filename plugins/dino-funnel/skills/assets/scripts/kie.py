"""Shared client for the kie.ai unified Jobs API.

kie.ai exposes most marketplace models (nano-banana, kling, grok-imagine, ...)
through one async job interface:

    POST /api/v1/jobs/createTask   {model, input}        -> taskId
    GET  /api/v1/jobs/recordInfo?taskId=...              -> state + resultJson

Vendored copy of the Kie jobs client; the key comes from KIE_API_KEY in the
environment or the nearest .env above the working folder. Needs `requests`.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

BASE_URL = "https://api.kie.ai/api/v1/jobs"


class KieError(Exception):
    """Any kie.ai jobs API failure (auth, credits, generation, timeout)."""


def _ensure_env_loaded() -> None:
    """Load KIE_API_KEY from the first .env found walking up from the working folder
    (the repo root, or the plugin user work folder)."""
    if os.environ.get("KIE_API_KEY") or os.environ.get("KIE_AI_API_KEY"):
        return
    for d in [Path.cwd(), *Path.cwd().parents]:
        env_path = d / ".env"
        if not env_path.is_file():
            continue
        with open(env_path, encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip("'\"")
                if v:
                    v = v.split("#", 1)[0].strip()
                if k and k not in os.environ:
                    os.environ[k] = v
        if os.environ.get("KIE_API_KEY"):
            return


def api_key() -> str:
    """The key or a clear exit: scripts call this instead of reading .env themselves."""
    key = get_api_key()
    if not key:
        raise SystemExit("KIE_API_KEY not found: put KIE_API_KEY=... in .env at the root of the working folder")
    return key


def get_api_key() -> str | None:
    """Return the kie.ai API key from the environment, if set."""
    _ensure_env_loaded()
    return os.environ.get("KIE_API_KEY") or os.environ.get("KIE_AI_API_KEY")


def _headers(api_key: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


def _request(method: str, url: str, *, retries: int = 4, **kwargs) -> Any:
    """HTTP request that retries transient network failures (dropped poll
    connections, timeouts) instead of letting one blip kill a long job.
    """
    import requests

    backoff = 2.0
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            return requests.request(method, url, **kwargs)
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.ChunkedEncodingError) as e:
            last_exc = e
            if attempt < retries:
                time.sleep(backoff)
                backoff = min(backoff * 2, 15)
                continue
    raise KieError(f"network error talking to kie.ai after {retries} tries: {last_exc}")


def _check_body_code(data: dict) -> None:
    """kie.ai returns logical errors as a `code` field inside an HTTP-200 body."""
    code = data.get("code")
    if code in (401, 403):
        raise KieError(f"kie.ai auth failed (code {code}) — check KIE_API_KEY: {data.get('msg')}")
    if code == 402:
        raise KieError(f"kie.ai out of credits (code 402): {data.get('msg')}")
    if code == 429:
        raise KieError(f"kie.ai rate limited (code 429): {data.get('msg')}")


def _raise_for_status(resp: Any) -> None:
    if resp.status_code == 401:
        raise KieError("kie.ai auth failed (401) — check KIE_API_KEY")
    if resp.status_code == 402:
        raise KieError("kie.ai has no remaining credits (402) — top up at kie.ai")
    if resp.status_code == 429:
        raise KieError("kie.ai rate limited (429)")
    if resp.status_code >= 400:
        raise KieError(f"kie.ai API error ({resp.status_code}): {resp.text[:300]}")


def create_task(
    api_key: str,
    model: str,
    inputs: dict[str, Any],
    max_retries: int = 5,
) -> str:
    """Submit a generation task and return its taskId.

    Retries on 429 with exponential backoff.
    """
    import requests

    url = f"{BASE_URL}/createTask"
    payload = {"model": model, "input": inputs}

    data = None
    for attempt in range(1, max_retries + 1):
        resp = _request("POST", url, json=payload, headers=_headers(api_key), timeout=60)
        if resp.status_code == 429 and attempt < max_retries:
            time.sleep(min(3 * attempt, 20))
            continue
        _raise_for_status(resp)
        data = resp.json()
        # kie.ai also signals rate limiting via a body `code` of 429 on HTTP 200
        if data.get("code") == 429 and attempt < max_retries:
            time.sleep(min(3 * attempt, 20))
            continue
        _check_body_code(data)
        break
    body = data.get("data") if isinstance(data.get("data"), dict) else data
    task_id = (body or {}).get("taskId") or data.get("taskId")
    if not task_id:
        raise KieError(f"No taskId in createTask response: {json.dumps(data)[:300]}")
    return task_id


def poll_task(
    api_key: str,
    task_id: str,
    timeout: float = 600.0,
    interval: float = 4.0,
) -> dict[str, Any]:
    """Poll recordInfo until the task succeeds, fails, or times out.

    Returns the task record dict (contains state, resultJson, creditsConsumed).
    """
    import requests

    url = f"{BASE_URL}/recordInfo"
    start = time.time()

    while True:
        if time.time() - start > timeout:
            raise KieError(f"kie.ai task {task_id} timed out after {timeout:.0f}s")

        resp = _request(
            "GET", url, params={"taskId": task_id}, headers=_headers(api_key), timeout=30
        )
        _raise_for_status(resp)
        data = resp.json()
        _check_body_code(data)
        record = data.get("data") if isinstance(data.get("data"), dict) else data
        state = str((record or {}).get("state", "")).lower()

        if state == "success":
            return record
        if state in ("fail", "failed", "error"):
            msg = (record or {}).get("failMsg") or json.dumps(record)[:300]
            raise KieError(f"kie.ai task {task_id} failed: {msg}")

        time.sleep(interval)


def result_urls(record: dict[str, Any]) -> list[str]:
    """Extract output media URLs from a successful task record."""
    raw = record.get("resultJson")
    if not raw:
        return []
    parsed = json.loads(raw) if isinstance(raw, str) else raw
    urls = parsed.get("resultUrls") or []
    if not urls and isinstance(parsed.get("resultObject"), dict):
        # Some models nest urls differently; surface anything URL-like.
        obj = parsed["resultObject"]
        for v in obj.values():
            if isinstance(v, list):
                urls.extend(u for u in v if isinstance(u, str))
    return urls


def download(url: str, dest_path: str | Path, timeout: float = 180.0) -> Path:
    """Stream a result URL to disk. Result URLs expire after ~24h, so call soon."""
    import requests

    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, stream=True, timeout=timeout)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    return dest


def run_job(
    api_key: str,
    model: str,
    inputs: dict[str, Any],
    output_path: str | Path,
    timeout: float = 600.0,
) -> dict[str, Any]:
    """End-to-end: create task, poll, download first result.

    Returns {"output_path", "result_url", "credits", "task_id"}.
    """
    task_id = create_task(api_key, model, inputs)
    record = poll_task(api_key, task_id, timeout=timeout)
    urls = result_urls(record)
    if not urls:
        raise KieError(f"kie.ai task {task_id} succeeded but returned no result URLs")
    out = download(urls[0], output_path)
    return {
        "output_path": str(out),
        "result_url": urls[0],
        "credits": record.get("creditsConsumed"),
        "task_id": task_id,
    }
