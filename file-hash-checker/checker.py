import hashlib
import sys
import json
from datetime import datetime

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        chunk = f.read(4096)
        while chunk:
            sha256.update(chunk)
            chunk = f.read(4096)
    return sha256.hexdigest()

def check_against_virustotal(file_hash):
    print(f"\n[*] Hash: {file_hash}")
    print(f"[*] Check manually: https://virustotal.com/gui/file/{file_hash}")
    print(f"[*] Or use VirusTotal API for automation")

def save_report(filepath, file_hash):
    report = {
        "file": filepath,
        "sha256": file_hash,
        "virustotal": f"https://virustotal.com/gui/file/{file_hash}",
        "timestamp": datetime.now().isoformat(),
        "mitre": "T1027 - Obfuscated Files or Information"
    }
    with open("hash_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print(f"[+] Report saved: hash_report.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 checker.py <filename>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f"[*] Scanning: {filepath}")
    file_hash = get_file_hash(filepath)
    print(f"[+] SHA256: {file_hash}")
    check_against_virustotal(file_hash)
    save_report(filepath, file_hash)

