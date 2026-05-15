import dns.resolver
import json
from datetime import datetime

# Target domain
TARGET = "google.com"

# Common subdomains wordlist
WORDLIST = [
    "www", "mail", "ftp", "admin", "dev",
    "test", "staging", "api", "blog", "shop",
    "portal", "vpn", "remote", "secure", "old"
]

# Results store karo
found = []

def check_subdomain(subdomain, domain):
    full_domain = f"{subdomain}.{domain}"
    try:
        answers = dns.resolver.resolve(full_domain, "A")
        for ip in answers:
            print(f"[FOUND] {full_domain} → {ip}")
            found.append({
                "subdomain": full_domain,
                "ip": str(ip),
                "timestamp": datetime.now().isoformat()
            })
    except dns.resolver.NXDOMAIN:
        print(f"[----] {full_domain}")
    except Exception:
        pass

def save_report():
    report = {
        "target": TARGET,
        "timestamp": datetime.now().isoformat(),
        "total_found": len(found),
        "subdomains": found
    }
    with open("subdomain_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print(f"\n[+] Report saved: subdomain_report.json")

if __name__ == "__main__":
    print(f"[*] Target: {TARGET}")
    print(f"[*] Wordlist: {len(WORDLIST)} subdomains")
    print(f"[*] Started: {datetime.now()}")
    print("-" * 50)
    
    for word in WORDLIST:
        check_subdomain(word, TARGET)
    
    print("-" * 50)
    print(f"[+] Found: {len(found)} subdomains")
    save_report()

