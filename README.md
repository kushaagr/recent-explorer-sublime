# Recent Explorer for Sublime Text
The *Recent Explorer* package provides a lightweight, project-dependent, keyboard-first dashboard view for [Sublime Text 4](http://sublimetext.com/).

Sublime Text is excellent at handling workspaces and project files. But it lacks one key feature: **a centralized, project-specific overview of your most recently modified assets.**

Recent Explorer fills this gap. It dynamically generates a dashboard tailored to your active project tree, allowing you to jump straight back into your flow.

Open the dashboard using the command palette or by positioning your cursor and using the default shortcuts.

## Features

Features provided by Recent Explorer:

- 📁 **Project-Dependent Context.** Dynamically adjusts its layout based on whatever project you are currently working in.
- ⚡ **Deep Code Discovery.** Automatically crawls down your project tree on launch to index your files.
- ⏳ **Intrinsic System Sorting.** Sorts files using true operating system metadata to reflect your actual workflow.
- 🎹 **Keyboard-First Navigation.** Seamlessly move up and down the dashboard list using intuitive keyboard shortcuts.
- 🖱️ **Mouse Action Support.** Double-click directly on any tracked item line to quickly open it.
- ⚙️ **Tailored Performance Boundaries.** Fully customizable scan parameters, allowing you to exclude specific directories.
- 🪶 **Zero Dependencies.** Built entirely with native Sublime Text APIs and Python—no heavy external binaries required.

Project management features built into Sublime Text:

* **Search for a file** with *Goto Anything* (**Command + P** or **Ctrl + P**).
* **Switch projects** with *Quick Switch Project* (**Ctrl + Alt + P**).

## Dashboard Layout

The dashboard structures your project by repository or root sub-paths, mapping out recent files alongside their last-modified timestamps:

```text
### <repository-name> [<local-path>]
 - [<YYYY-MM-DD HH:MM>] <relative-file-path>

```

For example:

```text
# Recent Explorer

## genesis-world [/Users/username/Python/genesis-world]
  - [2026-07-15 09:30:15] main.py
  - [2026-07-14 14:22:04] utils/helpers.py
  - [2026-07-12 11:05:45] config.json

## external-api [/Users/username/web/external-api]
  - [2026-07-15 08:12:00] index.js
  - [2026-07-10 18:45:12] package.json


```

Files are automatically tracked and refreshed on the dashboard whenever changes are written to disk.

## Commands

Recent Explorer provides these Sublime Text commands:

* **recent_explorer_open**: Opens the primary project dashboard view.
* Default keyboard map: **Ctrl + Alt + D** (Example placeholder)
* Default mouse map: **Double-Click** on an item line to open the file.


* **recent_explorer_refresh**: Manually triggers a re-crawl of the active project tree.

## Settings

Recent Explorer looks for settings in `RecentExplorer.sublime-settings`.

Recent Explorer supports these settings:

* **exclude_patterns**: Defines folder or file patterns (compatible with wildcards) that should be ignored during the project crawl. Example: `"exclude_patterns": ["node_modules", ".git", "__pycache__"]`.
* **scan_depth**: An integer defining how many directories deep the discovery engine should crawl from the project root. If not defined, it defaults to `3`. Example: `"scan_depth": 5`.


## 💾 Installation

### Manual Installation

Until this plugin is listed on Package Control, you can install it manually:

1. Open Sublime Text.
2. Go to **Preferences > Browse Packages...** to open your local packages folder.
3. Clone this repository directly into that folder:
```bash
git clone https://github.com/YOUR_USERNAME/recent-explorer-sublime.git ProjectDashboard

```

4. Restart Sublime Text.
