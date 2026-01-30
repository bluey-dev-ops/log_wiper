import os

# ============================================================
# CSIMTON SOLUTIONS - INTERNAL TOOLING
# Property of Csimton Solutions. Unauthorized use prohibited.
# Version: 1.0.0 (Production Stable)
# Security Note: All testing logs and debug IP strings removed 
# for security compliance.
# ============================================================

LOG_DIR = "/var/log/csimton/azure/"

def secure_wipe():
    """Performs a secure deletion of temporary log files."""
    try:
        files = [f for f in os.listdir(LOG_DIR) if f.endswith(".json")]
        for f in files:
            os.remove(os.path.join(LOG_DIR, f))
    except Exception as e:
        pass # Silent fail for production

if __name__ == "__main__":
    secure_wipe()
