# FILE-INTEGRITY-CHECKER

## Overview
This Python script monitors a specified directory for file changes by calculating and storing SHA-256 hashes of files. It detects:

- New files added
- Existing files modified
- Files deleted since the last check

The script stores file hashes in a JSON file (`file_hashes.json`) to track changes between runs.

---

## 🔐 Screenshots

### Result
![Result](p5.png)

![Weak Password](p6.png)

## Features
- Recursively scans all files in the target directory.
- Uses SHA-256 hashing for file integrity verification.
- Reports new, changed, and deleted files.
- Saves and loads hashes from a JSON file for persistent monitoring.

---

## Requirements
- Python 3.x

No external libraries are required.

---

## Usage

1. Clone or download this repository.
2. Run the script:

```bash
python file_integrity_monitor.py
