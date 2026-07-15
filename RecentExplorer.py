import sublime
import sublime_plugin
import os
from datetime import datetime

def get_file_metadata(file_path):
    """Extracts intrinsic system times and name data for a file path."""
    try:
        stat = os.stat(file_path)
        try:
            created_time = stat.st_birthtime
        except AttributeError:
            created_time = stat.st_ctime
        
        _, ext = os.path.splitext(file_path)
        return {
            "modified": stat.st_mtime,
            "created": created_time,
            "extension": ext.lower(),
            "name": os.path.basename(file_path)
        }
    except Exception:
        return None


# --- Event Listener for Auto-Refresh ---

class RecentExplorerListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        self._trigger_live_refresh(view)

    def on_new_async(self, view):
        self._trigger_live_refresh(view)

    def _trigger_live_refresh(self, view):
        """Automatically updates the dashboard view if active and enabled."""
        # Avoid infinite refresh loop if saving the dashboard itself
        if view.settings().get("recent_explorer_dashboard", False):
            return

        settings = sublime.load_settings("RecentExplorer.sublime-settings")
        if not settings.get("auto_refresh", True):
            return

        for window in sublime.windows():
            for v in window.views():
                if v.settings().get("recent_explorer_dashboard", False):
                    window.run_command("recent_explorer_open_dashboard", {"refresh_only": True})


# --- Core Command: Open/Render Project Dashboard ---

class RecentExplorerOpenDashboardCommand(sublime_plugin.WindowCommand):
    LINE_MAPS = {}

    def run(self, refresh_only=False):
        window = self.window
        
        # Load user configurations dynamically
        settings = sublime.load_settings("RecentExplorer.sublime-settings")
        sort_by = settings.get("sort_by", "created descending")
        max_files = settings.get("max_tracked_files_per_project", 200)
        ignored_dirs = set(settings.get("ignored_dirs", []))
        source_extensions = set([ext.lower() for ext in settings.get("source_extensions", [])])

        open_folders = window.folders()
        if not open_folders:
            sublime.status_message("Recent Explorer: No folders open in the project sidebar.")
            return

        dashboard_view = None
        for view in window.views():
            if view.settings().get("recent_explorer_dashboard", False):
                dashboard_view = view
                break

        if refresh_only and not dashboard_view:
            return

        if not dashboard_view:
            dashboard_view = window.new_file()
            dashboard_view.set_name("Project Dashboard")
            dashboard_view.set_scratch(True)
            dashboard_view.settings().set("recent_explorer_dashboard", True)
            dashboard_view.assign_syntax("Packages/Markdown/Markdown.sublime-syntax")

        self.render_project_dashboard(dashboard_view, open_folders, sort_by, ignored_dirs, source_extensions, max_files)

    def render_project_dashboard(self, view, open_folders, sort_by, ignored_dirs, source_extensions, max_files):
        grouped_data = {folder: [] for folder in open_folders}

        # Crawl open directories
        for folder in open_folders:
            for root, dirs, files in os.walk(folder):
                dirs[:] = [d for d in dirs if d not in ignored_dirs]
                
                for file in files:
                    _, ext = os.path.splitext(file)
                    if ext.lower() in source_extensions:
                        full_path = os.path.join(root, file)
                        meta = get_file_metadata(full_path)
                        if meta:
                            grouped_data[folder].append((full_path, meta))

        # Sort and truncate list per folder based on max_tracked_files_per_project setting
        for folder in open_folders:
            sorted_items = self.sort_items(grouped_data[folder], sort_by)
            grouped_data[folder] = sorted_items[:max_files]

        # Build dashboard layout text dynamically
        content = "# Project Dashboard\n\n"

        for folder in open_folders:
            folder_name = os.path.basename(folder)
            content += "## {0} [{1}]\n".format(folder_name, folder)
            
            if not grouped_data[folder]:
                content += "  (No source code files found matching settings profiles)\n\n"
                continue

            for path, meta in grouped_data[folder]:
                time_key = "created" if "created" in sort_by else "modified"
                time_str = datetime.fromtimestamp(meta[time_key]).strftime("%Y-%m-%d %H:%M:%S")
                relative_path = os.path.relpath(path, folder)
                content += "  - [{0}] {1}\n".format(time_str, relative_path)
            content += "\n"

        # Apply text safely
        view.set_read_only(False)
        view.run_command("recent_explorer_replace_text", {"text": content})
        view.set_read_only(True)

        # Build interactive line-to-file paths maps
        view_line_map = {}
        lines = content.splitlines()
        for i, line_text in enumerate(lines):
            if "  - [" in line_text:
                for folder in open_folders:
                    for path, _ in grouped_data[folder]:
                        rel_p = os.path.relpath(path, folder)
                        if rel_p in line_text:
                            view_line_map[i] = path
                            break

        RecentExplorerOpenDashboardCommand.LINE_MAPS[view.id()] = view_line_map

    def sort_items(self, items, sort_by):
        if not items:
            return []

        # We use negative numbers (-x) for timestamps to turn an ascending tuple 
        # sort into a descending (newest first) result.
        if sort_by == "modified descending":
            key_func = lambda x: (
                -x[1]["modified"],            # Primary (Newest first)
                -x[1]["created"],             # Secondary (Newest first)
                x[1]["name"].lower()          # Tertiary (A-Z)
            )
        elif sort_by == "modified ascending":
            key_func = lambda x: (
                x[1]["modified"],             # Primary (Oldest first)
                -x[1]["created"],             # Secondary (Newest first)
                x[1]["name"].lower()          # Tertiary (A-Z)
            )
        elif sort_by == "created ascending":
            key_func = lambda x: (
                x[1]["created"],              # Primary (Oldest first)
                -x[1]["modified"],            # Secondary (Newest first)
                x[1]["name"].lower()          # Tertiary (A-Z)
            )
        elif sort_by == "alphabetical":
            key_func = lambda x: (
                x[1]["name"].lower(),         # Primary (A-Z)
                -x[1]["created"],             # Secondary (Newest first)
                -x[1]["modified"]             # Tertiary (Newest first)
            )
        elif sort_by == "extension":
            key_func = lambda x: (
                x[1]["extension"],            # Primary (A-Z)
                -x[1]["created"],             # Secondary (Newest first)
                -x[1]["modified"],            # Tertiary (Newest first)
                x[1]["name"].lower()          # Quaternary (A-Z)
            )
        else:  # Default: "created descending"
            key_func = lambda x: (
                -x[1]["created"],             # Primary (Newest first)
                -x[1]["modified"],            # Secondary (Newest first)
                x[1]["name"].lower()          # Tertiary (A-Z)
            )

        return sorted(items, key=key_func)


# --- Helper Text Command for Buffer Injection ---

class RecentExplorerReplaceTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        self.view.replace(edit, sublime.Region(0, self.view.size()), text)


# --- Keyboard & Action Handler ---

class RecentExplorerActionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        view_id = view.id()

        if view_id not in RecentExplorerOpenDashboardCommand.LINE_MAPS:
            return

        selection = view.sel()[0]
        line_number, _ = view.rowcol(selection.begin())

        line_map = RecentExplorerOpenDashboardCommand.LINE_MAPS[view_id]
        target_file = line_map.get(line_number)

        if target_file and os.path.exists(target_file):
            window.open_file(target_file)