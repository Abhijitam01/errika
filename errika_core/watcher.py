import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .error_handler import is_error_line

class ErrorFileHandler(FileSystemEventHandler):
    def __init__(self,filepath ,  on_error_callback):
        self.filepath = filepath
        self.on_error_callback = on_error_callback
        self._last_position = 0

    def on_modified(self, event):
        if event.src_path != self.filepath:
            return
        
        with open(self.filepath, 'r') as f:
            f.seek(self._last_position)
            new_lines = f.readlines()
            self._last_position = f.tell()

        for line in new_lines:
            if is_error_line(line):
                self.on_error_callback(line.strip())
    def start_watching(error_file_path , on_error_callback):
        event_handler = ErrorFileHandler(error_file_path , on_error_callback)
        observer = Observer()
        observer.schedule(event_handler, path=error_file_path, recursive=False)
        observer.start()
        try:
            print(f"Watching for changes in {error_file_path}...")
            # Keep the script running
            # until interrupted
            # This is a blocking call, so it will keep the script running
            # until interrupted
            # You can also use a while loop with a sleep to keep the script running
            # without blocking the main thread
            # For example:
            # while True:
            #     time.sleep(1)
            # This is a blocking call, so it will keep the script running   
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("Stopped watching for changes.")
        observer.join()