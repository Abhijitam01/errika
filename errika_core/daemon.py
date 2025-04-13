import os 
from .watcher import start_watching

def handle_error(error_line : str):
    print("\n New error detected:")
    print(error_line)
    # Here you can add your custom error handling logic

def run_daemon():
    # Get the path to the error log file
    error_log_path = os.path.abspath(os.path.dirname("sample_error_log.txt"))
    
    if not os.path.exists(error_log_path):
        print(f"Error log file {error_log_path} does not exist. Creating it ...")
        open(error_log_path, 'w').close()
    start_watching(error_log_path , handle_error)