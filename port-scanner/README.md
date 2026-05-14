# Port Scanner

A Python tool that scans all ports on a target machine to detect 
which ports are open and which services are running on them.
Built to understand how attackers perform reconnaissance 
and how SOC analysts detect open attack surfaces.

## Features
- Scans ports 1-1024 on any target IP
- Banner grabbing — identifies which service is running on each open port
- Generates JSON report with findings and timestamps

## What I Learned
- TCP 3-way handshake (SYN, SYN-ACK, ACK) and how port scanning works
- Banner grabbing is critical because open port alone is not enough —
  SOC analysts need to know WHAT is running to detect suspicious services
- Python socket library for real network connections

## MITRE ATT&CK
- Technique: T1046 - Network Service Discovery

## Usage
python3 scan.py

## Sample Output
[OPEN] Port 22  | SSH-2.0-OpenSSH_10.2p1 Debian-6
[OPEN] Port 443 | No banner
[+] Report saved: scan_report.json
