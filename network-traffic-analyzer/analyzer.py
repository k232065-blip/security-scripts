from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import defaultdict
from datetime import datetime
import json

# Traffic counters
ip_counter = defaultdict(int)
protocol_counter = defaultdict(int)
suspicious = []

# Protocol map
PROTOCOLS = {6: "TCP", 17: "UDP", 1: "ICMP", 2: "IGMP"}

def analyze_packet(pkt):
    if IP not in pkt:
        return
    
    src = pkt[IP].src
    dst = pkt[IP].dst
    proto = pkt[IP].proto
    proto_name = PROTOCOLS.get(proto, "UNKNOWN")
    
    # Count karo
    ip_counter[src] += 1
    protocol_counter[proto_name] += 1
    
    # Print karo
    print(f"[{datetime.now().strftime('%H:%M:%S')}] "
          f"{src} -> {dst} | {proto_name}")
    
    # Suspicious check
    if ip_counter[src] > 50:
        alert = f"[ALERT] DDoS? {src} sent {ip_counter[src]} packets!"
        if alert not in suspicious:
            suspicious.append(alert)
            print(alert)

def start_capture(count=50):
    print(f"[*] Starting capture — {count} packets")
    print(f"[*] Time: {datetime.now()}")
    print("-" * 50)
    sniff(count=count, prn=analyze_packet, store=0)
    print("-" * 50)
    print(f"\n[+] Top Talkers:")
    for ip, count in sorted(ip_counter.items(), 
                            key=lambda x: x[1], reverse=True)[:5]:
        print(f"    {ip} → {count} packets")
    print(f"\n[+] Protocols seen:")
    for proto, count in protocol_counter.items():
        print(f"    {proto} → {count} packets")
      # JSON report save karo
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_packets": sum(protocol_counter.values()),
        "protocols": dict(protocol_counter),
        "top_talkers": dict(sorted(ip_counter.items(),
                           key=lambda x: x[1], reverse=True)[:5]),
        "suspicious_alerts": suspicious
    }
    with open("traffic_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print(f"\n[+] Report saved: traffic_report.json")

if __name__ == "__main__":
    start_capture(count=50)
