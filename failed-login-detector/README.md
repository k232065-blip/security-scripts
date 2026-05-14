# Failed Login Detector

A Python-based SOC tool that parses Linux auth logs to detect 
brute force login attempts and generates JSON incident reports.

## MITRE ATT&CK
- Technique: T1110 - Brute Force
- Tactic: Credential Access

## Features
- Parses auth.log for failed SSH login attempts
- Flags attacker IPs with severity levels (LOW/MEDIUM/HIGH/CRITICAL)
- Identifies targeted usernames
- Generates JSON incident report automatically

## Thresholds
| Attempts | Severity |
|----------|----------|
| 1-4      | LOW      |
| 5-9      | MEDIUM   |
| 10-19    | HIGH     |
| 20+      | CRITICAL |

## Usage
```bash
python3 detector.py
```

## Sample Output
python3 detector.py
[MEDIUM] IP: 192.168.1.100 | Attempts: 7 | Users targeted: {'root'}
[LOW] IP: 45.33.32.156 | Attempts: 2 | Users targeted: {'admin'}
[HIGH] IP: 172.16.0.50 | Attempts: 10 | Users targeted: {'test'}

[+] Report saved: incident_report.json

