# main.py
from whois_lookup import get_domain_info
from blackbox_recon import black_box_recon
from port_scanner import scan_ports
from nmap_scan import nmap_scan

def run_all():
    print("\n=== WHOIS LOOKUP ===")
    get_domain_info("python.com")

    print("\n=== BLACK BOX RECON ===")
    black_box_recon("http://python.com")

    print("\n=== BASIC PORT SCAN ===")
    ports = [80, 443, 22, 8080]
    result = scan_ports("127.0.0.1", ports)
    print(f"Open Ports: {result}")

    print("\n=== NMAP ADVANCED SCAN ===")
    nmap_scan("127.0.0.1", "1-20")

if __name__ == "__main__":
    run_all()