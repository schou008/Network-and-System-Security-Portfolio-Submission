import os
import hashlib
import csv
from datetime import datetime

TARGET_FOLDER = "test_files"
BASELINE_FILE = "baseline.csv"

def hash_file(path):
    """Generate SHA-256 hash of a file."""
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

def generate_baseline():
    """Scans a folder, hashes files, and saves baseline CSV."""
    if not os.path.isdir(TARGET_FOLDER):
        print(f"Target folder '{TARGET_FOLDER}' not found. Create it and add files before running.")
        return

    files = sorted(os.listdir(TARGET_FOLDER))

    with open(BASELINE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "sha256", "timestamp"])

        for file in files:
            full_path = os.path.join(TARGET_FOLDER, file)

            if os.path.isfile(full_path):
                file_hash = hash_file(full_path)
                timestamp = datetime.now().isoformat()

                writer.writerow([file, file_hash, timestamp])
                print(f"[OK] {file} → {file_hash}")

    print("\\nBaseline saved to", BASELINE_FILE)

if __name__ == "__main__":
    print("=== Section 1: File Integrity Checker ===")
    generate_baseline()