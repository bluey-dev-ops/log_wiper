import os
import time

# log_wiper.py v0.2
# Added Verbose logging and error handling

LOG_DIR = "./logs/azure_exports/"

def clear_logs(verbose=False):
    if not os.path.exists(LOG_DIR):
        print("Error: Log directory not found.")
        return

    for filename in os.listdir(LOG_DIR):
        if filename.endswith(".json"):
            if verbose:
                print(f"Processing: {filename}")
            os.remove(os.path.join(LOG_DIR, filename))

if __name__ == "__main__":
    # Test run initiated by Bluey
    clear_logs(verbose=True)
