# Recent Explorer - Project Dashboard for Sublime Text

A lightweight, project-dependent, keyboard-first dashboard view for Sublime Text 4. 
It dynamically surfaces your project source code files organized by sidebar directories, 
sorted by intrinsic system creation or modification times, and indexed instantly without blocking your editor.


```text
# Recent Explorer

## genesis-world [/Users/username/Python/genesis-world]
  - [2026-07-15 09:30:15] main.py
  - [2026-07-14 14:22:04] utils/helpers.py
  - [2026-07-12 11:05:45] config.json

## external-api [/Users/username/Python/external-api]
  - [2026-07-15 08:12:00] index.js
  - [2026-07-10 18:45:12] package.json

```

---

## ✨ Features

* 📁 **Project-Dependent Context:** Dynamically adjusts its layout based on whatever root folders are currently open in your active sidebar.
* ⚡ **Deep Code Discovery:** Automatically crawls down your project tree on launch to surface source files immediately—no manual tracking history required.
* ⏳ **Intrinsic System Sorting:** Sort files using true operating system metadata (Creation Time, Modification Time, Alphabetical, or Extension grouping).
* 🎹 **Keyboard-First Navigation:** Seamlessly move up and down the dashboard list using standard arrow keys and press `Enter` to open the targeted file instantly.
* 🖱️ **Mouse Action Support:** Double-click directly on any tracked item line to quickly switch your editor workspace focus to that file.
* ⚙️ **Tailored Performance Boundaries:** Fully customizable scan parameters. Exclude heavy directories (like `node_modules` or `.git`) and define specific file extensions via user settings.
* 🪶 **Zero Dependencies:** Built entirely with native Sublime Text APIs and Python standard libraries. Lightweight execution that never lags the UI thread.

---

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

---

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

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.