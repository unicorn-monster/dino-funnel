---
name: funnel-setup
description: One-time setup of this computer for the dino-funnel plugin: work folder, Kie API key, Python packages, cwebp/ffmpeg, Shopify CLI login to the Dino store, Chrome remote debugging. Use when the user runs /dino-funnel:funnel-setup, says "cài đặt", "setup", "lần đầu dùng", or a funnel step fails because a tool, key or login is missing.
---

# Funnel setup (run once per computer)

The user is not technical: do every step yourself, explain in one short Vietnamese line what you're doing, and only ask them for what only they can do (paste a key, log in, flip a Chrome switch). Re-running is safe: skip what is already done. End with a checklist table: item, ok / not ok, what to do.

1. **Work folder.** Everything runs from one folder, default `~/dino-work`. Ask if they want another place. Create it with `output/` inside. Copy `${CLAUDE_PLUGIN_ROOT}/skills/funnel-setup/templates/CLAUDE.md` into it as `CLAUDE.md` if there isn't one. Tell them: always open Claude Code in this folder (Claude app → Code → choose folder).
2. **Kie key.** If `<work folder>/.env` has no `KIE_API_KEY=`, ask them to paste their kie.ai API key (kie.ai → API Key) and write `KIE_API_KEY=<key>` to `.env`. Test: `cd <work folder> && python3 -c "import sys; sys.path.insert(0, '${CLAUDE_PLUGIN_ROOT}/skills/assets/scripts'); import kie; kie.api_key(); print('ok')"`.
3. **Homebrew** (`brew --version`). Missing: tell them to install it from brew.sh (needs their Mac password, so they run it in Terminal themselves) and wait.
4. **Tools:** `brew install webp ffmpeg node python` for whatever is missing (`cwebp`, `ffmpeg`, `node`, `python3`).
5. **Python packages:** `python3 -c "import requests, PIL"`; missing → `python3 -m pip install --user requests Pillow`, and if pip refuses (externally managed) add `--break-system-packages`. Re-test.
6. **Shopify CLI** (`shopify version`). Missing: `npm install -g @shopify/cli@latest`. Login: `shopify store auth --store dinosaurized-army-store.myshopify.com --scopes read_files,write_files` opens the browser; they log in with the staff account Huy gave them. Test: `shopify store execute --store dinosaurized-army-store.myshopify.com --query '{shop{name}}'`.
7. **Chrome** (Amazon research and page checks drive their real Chrome through the chrome-devtools MCP that ships with this plugin). Open `chrome://inspect/#remote-debugging` (`osascript -e 'tell application "Google Chrome" to open location "chrome://inspect/#remote-debugging"'`), ask them to turn the switch on, and to stay logged in to Amazon in that Chrome. Test: list pages with the chrome-devtools MCP. If its tools don't show up, ask them to restart Claude Code.
8. **Done.** Tell them how to start: `/dino-funnel:funnel <amazon link> <offer link>`.
