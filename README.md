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

## 🚀 Usage

### Opening the Dashboard

1. Open the Sublime Text Command Palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS).
2. Type **`Recent Explorer: Open Dashboard`** and hit `Enter`.
3. A scratch tab named `Recent Explorer` will open, displaying your files separated by project root folder.

### Interaction Rules

* **Open File (Keyboard):** Navigate your cursor to any file line using the arrow keys and press `Enter`.
* **Open File (Mouse):** Double-click directly on the file entry line.
* **Auto-Refresh:** The dashboard will dynamically regenerate in the background whenever you create a new file or save changes to an existing project document.

---

## ⚙️ Configuration
You can customize the plugin's crawling filters, truncation limits, and sorting mechanics by navigating to **Preferences > Package Settings > RecentExplorer > Settings**.

Here is the default configuration schema:

```json
{
    // The sorting algorithm to use on the dashboard.
    // Options: "created descending", "created ascending", "modified descending", 
    //          "modified ascending", "alphabetical", "extension"
    "sort_by": "created descending",

    // Automatically refresh the dashboard tab when files are saved or created elsewhere
    "auto_refresh": true,

    // Cap the maximum number of items listed per project folder to maintain scannability
    "max_tracked_files_per_project": 200,

    // Directory names that the crawler will completely skip over for performance speed
    "ignored_dirs": [
        ".git", ".svn", "node_modules", "__pycache__", 
        "env", "venv", ".venv", "build", "dist", "target"
    ],

    // File extensions targeted for inclusion in your workspace overview
    "source_extensions": [
        ".py", ".js", ".ts", ".jsx", ".tsx", ".json", ".md", ".txt", ".html", 
        ".css", ".scss", ".rs", ".go", ".c", ".cpp", ".h", ".hpp", ".java", 
        ".kt", ".php", ".rb", ".sh", ".yaml", ".yml", ".ini", ".conf"
    ]
}
```

---

## 🛠️ Sorting Criteria Options

| Setting Parameter | Behavior Description |
| --- | --- |
| `"created descending"` | Surfaces the newest files created on your operating system first **(Default)**. |
| `"created ascending"` | Lists files starting from the oldest creation date. |
| `"modified descending"` | Prioritizes files you edited and saved most recently. |
| `"modified ascending"` | Displays project files based on the oldest edit footprint timestamp. |
| `"alphabetical"` | Lists files using standard alphanumeric A-Z character matching. |
| `"extension"` | Groups files chronologically by their common formats (`.js`, `.py`, etc.). |


## 💾 Installation

### Manual Installation

Until this plugin is listed on Package Control, you can install it manually:

1. Open Sublime Text.
2. Go to **Preferences > Browse Packages...** to open your local packages folder.
3. Clone this repository directly into that folder:
```bash
git clone https://github.com/kushaagr/recent-explorer-sublime.git RecentExplorer
```
4. Restart Sublime Text.
