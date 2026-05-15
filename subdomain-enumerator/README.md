# Subdomain Enumerator

A Python tool that finds subdomains of a target domain by resolving
DNS A records. Used for reconnaissance to map an organization's 
digital footprint and identify forgotten or exposed subdomains.

## Features
- Subdomain enumeration using wordlist
- DNS A record lookup — resolves IP addresses
- Detects multiple IPs per subdomain (load balancing)
- JSON report generation
- Clean terminal output — FOUND vs not found

## MITRE ATT&CK
- Technique: T1590 - Gather Victim Network Information

## Usage
python3 enumerator.py

## What I Learned
- DNS A Record — domain ko IPv4 address mein convert karta hai
- Subdomain reconnaissance — dev/test/admin subdomains 
  often expose vulnerable systems
- NXDOMAIN — subdomain exist nahi karta
- Python dns.resolver library

## Sample Output
[FOUND] www.google.com → 142.251.153.119
[FOUND] admin.google.com → 142.250.202.14
[----] dev.google.com
[+] Found: 19 subdomains
[+] Report saved: subdomain_report.json
