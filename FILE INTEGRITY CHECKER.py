import hashlib
import os
import json

HASH_FILE = 'file_hashes.json'

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

def check_files(directory):
    stored_hashes = load_hashes()
    current_hashes = {}
    changed_files = []
    new_files = []
    deleted_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = calculate_hash(path)
            if file_hash:
                current_hashes[path] = file_hash


    for path, file_hash in current_hashes.items():
        if path not in stored_hashes:
            new_files.append(path)
        elif stored_hashes[path] != file_hash:
            changed_files.append(path)


    for path in stored_hashes:
        if path not in current_hashes:
            deleted_files.append(path)

    save_hashes(current_hashes)

    return new_files, changed_files, deleted_files

if __name__ == '__main__':
    directory_to_monitor = input("Enter the directory to monitor: ").strip()
    new_files, changed_files, deleted_files = check_files(directory_to_monitor)

    if new_files:
        print("New files detected:")
        for f in new_files:
            print(f"  {f}")

    if changed_files:
        print("Changed files detected:")
        for f in changed_files:
            print(f"  {f}")

    if deleted_files:
        print("Deleted files detected:")
        for f in deleted_files:
            print(f"  {f}")

    if not (new_files or changed_files or deleted_files):
        print("No changes detected.")
