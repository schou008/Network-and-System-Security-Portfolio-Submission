import random
import time
from datetime import datetime

def simulate_network_monitor():
    print("=== Simple Network Monitor ===\\n")

    THRESHOLD = 10  # too many outbound connections = suspicious

    try:
        while True:
            outbound = random.randint(1, 20)
            now = datetime.now().isoformat(timespec='seconds')
            print(f"[{now}] Outbound connections: {outbound}")

            if outbound > THRESHOLD:
                print("[ALERT] Suspicious network activity detected!\\n")
            else:
                print("Normal activity.\\n")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\\nMonitoring stopped by user.")

if __name__ == "__main__":
    simulate_network_monitor()