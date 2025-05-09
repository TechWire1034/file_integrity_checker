import hashlib
import os

def calculate_file_hash(filename):
    """Calculate SHA-256 hash of a file."""
    try:
        sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            # Read file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        return f"Error: {str(e)}"

def save_hash(filename, file_hash):
    """Save filename and hash to file_hashes.txt."""
    with open("file_hashes.txt", "a") as f:
        f.write(f"{filename}: {file_hash}\n")

def verify_file_integrity(filename, original_hash):
    """Verify file integrity by comparing current hash to original."""
    current_hash = calculate_file_hash(filename)
    if current_hash is None:
        return f"Error: File '{filename}' not found."
    if isinstance(current_hash, str) and current_hash.startswith("Error"):
        return current_hash
    return current_hash == original_hash, current_hash

# Main program
print("File Integrity Checker (SHA-256)")
filename = input("Enter the file path to check (e.g., document.txt): ")

# Check if file exists
if not os.path.isfile(filename):
    print(f"Error: File '{filename}' not found.")
    exit(1)

# Calculate and display hash
file_hash = calculate_file_hash(filename)
if file_hash is None:
    print(f"Error: File '{filename}' not found.")
    exit(1)
if isinstance(file_hash, str) and file_hash.startswith("Error"):
    print(file_hash)
    exit(1)

print(f"\nSHA-256 Hash: {file_hash}")

# Save hash to file
save_hash(filename, file_hash)
print(f"Hash saved to 'file_hashes.txt'.")

# Optional: Verify against a known hash
verify = input("\nDo you want to verify against a known hash? (y/n): ").lower()
if verify == "y":
    known_hash = input("Enter the known SHA-256 hash: ").strip()
    is_valid, current_hash = verify_file_integrity(filename, known_hash)
    if isinstance(is_valid, str):
        print(is_valid)
    else:
        if is_valid:
            print("Integrity Check: File is unchanged (hashes match).")
        else:
            print(f"Integrity Check: File has changed!\nCurrent Hash: {current_hash}\nKnown Hash: {known_hash}")