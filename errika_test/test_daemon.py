import os
from watcher import start_watching

def run():
    log_path = os.path.abspath("sample_error.log")

    if not os.path.exists(log_path):
        print("Creating log file...")
        open(log_path, "w").close()

    start_watching(log_path)

if __name__ == "__main__":
    run()
