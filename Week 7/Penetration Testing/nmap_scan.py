# nmap_scan.py
import nmap

def nmap_scan(host, port_range="1-1024"):
    nm = nmap.PortScanner()
    try:
        nm.scan(host, port_range, arguments="-sV")  # Service/version detection

        for h in nm.all_hosts():
            print(f"\nHost: {h} ({nm[h].hostname()})")
            print(f"State: {nm[h].state()}")

            for proto in nm[h].all_protocols():
                print(f"\nProtocol: {proto}")
                lport = nm[h][proto].keys()

                for port in sorted(lport):
                    svc = nm[h][proto][port]
                    print(f"Port: {port}\tState: {svc['state']}\tService: {svc.get('name')} {svc.get('version', '')}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    nmap_scan("127.0.0.1", "1-10")