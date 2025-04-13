import os
from .watcher import start_watching
from .llm_client import simplify_error


def handle_error(error_line):
    print("\n🚨 New Error Detected:")
    print(error_line)
    print("💡 Asking OpenAI for help...\n")
    simplified = simplify_error(error_line)
    print("🧠 Simplified Error:")
    print(simplified)
    print("\n" + "="*50 + "\n")


def run_daemon():
    error_log_path = os.path.abspath("sample_error.log")

    if not os.path.exists(error_log_path):
        print("📁 Creating sample_error.log...")
        open(error_log_path, "w").close()

    start_watching(error_log_path, handle_error)


if __name__ == "__main__":
    run_daemon()
