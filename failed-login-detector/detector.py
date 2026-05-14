import re
from collections import defaultdict

LOG_FILE = "sample_auth.log"
THRESHOLD = 5

ip_count = defaultdict(int)
ip_users = defaultdict(set)

# Regex pattern
pattern = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from ([\d.]+)"
)

# Log file read karo
with open(LOG_FILE, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            user = match.group(1)
            ip   = match.group(2)
            ip_count[ip] += 1
            ip_users[ip].add(user)

# Alert levels
for ip, count in ip_count.items():
    if count >= 20:
        level = "CRITICAL"
    elif count >= 10:
        level = "HIGH"
    elif count >= 5:
        level = "MEDIUM"
    else:
        level = "LOW"

    print(f"[{level}] IP: {ip} | Attempts: {count} | Users targeted: {ip_users[ip]}")
import json
from datetime import datetime

# JSON report banao
report = []
for ip, count in ip_count.items():
    if count >= 20:
        level = "CRITICAL"
    elif count >= 10:
        level = "HIGH"
    elif count >= 5:
        level = "MEDIUM"
    else:
        level = "LOW"
    
    report.append({
        "ip": ip,
        "attempts": count,
        "users_targeted": list(ip_users[ip]),
        "severity": level,
        "mitre": "T1110 - Brute Force",
        "timestamp": datetime.now().isoformat()
    })

# File mein save karo
with open("incident_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\n[+] Report saved: incident_report.json")
