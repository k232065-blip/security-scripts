import socket
import json
from datetime import datetime

TARGET = "127.0.0.1"
PORTS  = range(1, 1025)
open_ports = []

print(f"Scanning {TARGET}...")
print(f"Started: {datetime.now()}")
print("-" * 40)

for port in PORTS:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((TARGET, port))
    if result == 0:
        banner = ""
        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode().strip()
            banner = banner.split("\n")[0]
        except:
            banner = "No banner"
        print(f"[OPEN] Port {port} | {banner}")
        open_ports.append({
            "port": port,
            "banner": banner,
            "timestamp": datetime.now().isoformat()
        })
    sock.close()

print("-" * 40)
print(f"Done: {datetime.now()}")

with open("scan_report.json", "w") as f:
    json.dump({"target": TARGET, "open_ports": open_ports}, f, indent=4)

print("[+] Report saved: scan_report.json")
