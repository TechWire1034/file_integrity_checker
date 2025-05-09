# SHA-256 File Integrity Checker
A Python script to verify the integrity of files by calculating their SHA-256 hash and comparing it to a known value.

## Features
- Calculates SHA-256 hash of a file in chunks (efficient for large files).
- Saves the hash to `file_hashes.txt`.
- Optionally verifies the file against a known hash.
- Includes error handling for missing files or other issues.

## Usage
1. Clone this repository: `git clone https://github.com/TechWire1034/file_integrity_checker.git`
2. Navigate to the folder: `cd file_integrity_checker`
3. Run the script: `python file_integrity_checker.py`
4. Enter the file path to check (e.g., `mini.iso`).
5. View the calculated hash and save it to `file_hashes.txt`.
6. Optionally verify against a known hash.

## Example
Used to verify Ubuntu 18.04 `mini.iso` (~57MB) with hash `54ad96248f6aa7b395763d37bb8524f6971a2a456d51fbe0085f82d26bee0`. Download `mini.iso` from [here](http://archive.ubuntu.com/ubuntu/dists/bionic/main/installer-amd64/current/images/netboot/).

## Author
GitHub: [TechWire1034](https://github.com/TechWire1034)
