# Network Traffic Analyzer

A Python tool that captures and analyzes live network traffic
to detect suspicious activity and identify top talkers on the network.
Built using Scapy for real-time packet inspection.

## Features
- Captures live packets and analyzes them in real-time with timestamps
- Identifies top talkers — which IP is sending the most packets
- Protocol breakdown — TCP, UDP, ICMP, IGMP packet counts
- Detects suspicious traffic — flags IPs sending abnormal packet volume
- Saves JSON report with full analysis summary

## MITRE ATT&CK
- Technique: T1040 - Network Sniffing

## Usage
sudo python3 analyzer.py

## What I Learned
- How to capture live network packets using Scapy
- TCP, UDP, ICMP, IGMP protocols and their differences
- How SOC analysts identify suspicious traffic using baseline comparison
- Alert deduplication — same alert sirf ek baar print ho
- Why raw packet capture needs root/sudo permissions

## Sample Output
[03:29:31] 192.168.100.69 -> 142.251.37.78 | ICMP
[03:29:35] 192.168.100.69 -> 199.165.136.100 | TCP

[+] Top Talkers:
    192.168.100.69 → 16 packets

[+] Protocols seen:
    TCP → 31 packets
    UDP → 16 packets
[+] Report saved: traffic_report.json
