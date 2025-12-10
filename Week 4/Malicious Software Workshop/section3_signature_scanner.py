import os
import re

TARGET_FOLDER = "test_files"

SIGNATURES = [
    r"eval\(",
    r"exec\(",
    r"base64\.b64decode",
    r"socket\.connect",
    r"import os"
]

def scan_file(path):
    try:
        with open(path, "r", errors="ignore", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        # binary or unreadable; skip textual scan
        return []

    matches = []
    for sig in SIGNATURES:
        if re.search(sig, content):
            matches.append(sig)
    return matches

def scan_folder():
    print("=== Signature Scan ===\\n")

    for file in sorted(os.listdir(TARGET_FOLDER)):
        path = os.path.join(TARGET_FOLDER, file)

        if os.path.isfile(path):
            matches = scan_file(path)

            if matches:
                print(f"[SUSPECT] {file} → {matches}")
            else:
                print(f"[CLEAN] {file}")

if __name__ == "__main__":
    if not os.path.isdir(TARGET_FOLDER):
        print(f"Target folder '{TARGET_FOLDER}' not found. Create it and add files before running.")
    else:
        scan_folder()