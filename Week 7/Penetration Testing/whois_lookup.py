# whois_lookup.py
import socket
import requests

def get_domain_info(domain):
    try:
        # Get IP address of the domain (active but low‑risk)
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")

        # WHOIS-like info using the free ipapi.co API
        response = requests.get(f"https://ipapi.co/{ip}/json/")

        if response.status_code == 200:
            data = response.json()
            print(f"Organization: {data.get('org', 'Unknown')}")
            print(f"City: {data.get('city', 'Unknown')}")
            print(f"Country: {data.get('country_name', 'Unknown')}")
        else:
            print("Could not fetch WHOIS data.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("\n=== WHOIS Lookup ===")
    get_domain_info("python.com")