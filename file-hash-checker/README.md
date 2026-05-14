# File Hash Checker

A Python tool that scans any file, generates its SHA256 hash,
and provides a VirusTotal link to check if the file is malicious.
Used by SOC analysts to detect tampered or malicious files.

## Features
- Generates SHA256 hash of any file
- Provides direct VirusTotal link for manual analysis
- Saves JSON report with hash, timestamp, and MITRE mapping

## MITRE ATT&CK
- Technique: T1027 - Obfuscated Files or Information

## Usage
python3 checker.py <filename>

## What I Learned
- Avalanche Effect — changing one character completely changes the hash
- hashlib library for SHA256 implementation in Python
- sys.argv for passing command line arguments
- Reading files in binary mode (rb) with chunks for large files

## Sample Output
[*] Scanning: test_file.txt
[+] SHA256: 1612e6ed247649076518d65935a5fd8ba2cfe4b7c2119dc38cd06659acec1f98
[*] Check manually: https://virustotal.com/gui/file/1612e6ed...
[+] Report saved: hash_report.json
