import os
import csv
import hashlib

TARGET_FOLDER = "test_files"
BASELINE_FILE = "baseline.csv"

def hash_file(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            block = f.read(4096)
            if not block:
                break
            sha.update(block)
    return sha.hexdigest()

def load_baseline():
    baseline = {}
    if not os.path.exists(BASELINE_FILE):
        print("Baseline file not found. Run section1_file_integrity_checker.py first to create baseline.csv")
        return baseline

    with open(BASELINE_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for filename, filehash, timestamp in reader:
            baseline[filename] = filehash
    return baseline

def detect_changes():
    baseline = load_baseline()
    if not baseline:
        return

    current_files = sorted(os.listdir(TARGET_FOLDER))

    print("=== Checking for changes ===\\n")

    # Detect modified or unchanged files
    for file in current_files:
        full_path = os.path.join(TARGET_FOLDER, file)

        if os.path.isfile(full_path):
            new_hash = hash_file(full_path)

            if file not in baseline:
                print(f"[NEW] File added: {file}")
            elif baseline[file] != new_hash:
                print(f"[MODIFIED] {file}")
            else:
                print(f"[OK] {file} unchanged")

    # Detect deleted files
    for file in baseline:
        if file not in current_files:
            print(f"[DELETED] {file}")

if __name__ == "__main__":
    detect_changes()