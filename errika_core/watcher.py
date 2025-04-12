import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .error_handler import is_error_line