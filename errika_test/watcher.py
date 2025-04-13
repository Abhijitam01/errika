import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ErrorFileHandler(FileSystemEventHandler):
    def __init__(self, filepath):
        self.filepath = filepath
        self._last_position = 0

    def on_modified(self, event):
        print(f"🔁 File modified: {event.src_path}")
        if os.path.abspath(event.src_path) != os.path.abspath(self.filepath):
            print("❌ Not the file we're watching")
            return

        with open(self.filepath, 'r') as f:
            f.seek(self._last_position)
            new_lines = f.readlines()
            self._last_position = f.tell()

        for line in new_lines:
            print(f"🆕 New line: {line.strip()}")


def start_watching(error_file_path):
    event_handler = ErrorFileHandler(error_file_path)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(error_file_path), recursive=False)
    observer.start()

    print(f"🟢 Watching {error_file_path} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Stopped watching.")
    observer.join()
