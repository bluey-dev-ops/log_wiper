import os
import time

# log_wiper.py v0.1
# Simple utility to clear local Azure log exports to save disk space.

LOG_DIR = "./logs/azure_exports/"

def clear_logs():
    print(f"Scanning {LOG_DIR} for legacy JSON logs...")
    # TODO: Implement Graph API connection for remote wiping
    for filename in os.listdir(LOG_DIR):
        if filename.endswith(".json"):
            print(f"Removing {filename}...")
            # os.remove(os.path.join(LOG_DIR, filename))

if __name__ == "__main__":
    clear_logs()
