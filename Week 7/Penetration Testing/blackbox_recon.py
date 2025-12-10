# blackbox_recon.py
import requests

def black_box_recon(url):
    try:
        response = requests.head(url)
        print("\n=== Black Box Findings ===")
        print(f"Server: {response.headers.get('Server', 'Unknown')}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    black_box_recon("http://python.com")