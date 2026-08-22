# ShotSplitter

Maya tool for splitting a single animated shot file into per-sub-shot `.ma`
files, each re-based to start at frame 1001 (keyframes offset/trimmed to the
new range, audio ranges re-synced).

## Structure

- `plugin.py` — UkoreHub host-app entry point (`register(api)`). Contributes
  `maya-scripts/` to `PYTHONPATH` and a `launch_hooks` entry (via the
  `maya_launcher_env_bridge` project plugin config store) so `ShotSplitter`
  auto-imports on Maya's first file-open, registering its menu item.
- `maya-scripts/ShotSplitter/` — the Maya-side package (runs inside Maya's
  own interpreter, not the UkoreHub app process — imports `core.*`-style
  Maya toolkit modules directly, not `plugin_api`).
  - `__init__.py` — registers the "Shot Splitter..." item under Ukore
    Tools > **Anim**, plus a reload handler, via `UkoreMenu`.
  - `interface.py` — `MainWindow` (Qt UI) and `show()` launcher.
  - `function.py` — keyframe/time-range/audio editing helpers.
  - `ui.ui` — Qt Designer layout.

## Requires

- `maya_toolkit` (`tmlib`, `UkoreMaya.core.template_ui`)
- `ukore_menu` (`UkoreMenu` menu registry)

See `ukore_menu`'s own docs for the full menu-registration contract this
plugin follows.
