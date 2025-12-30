import socket
import threading
from datetime import datetime

# Port Scan Function
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

# Main Program
target = input("Enter the IP or Hostname to scan: ")
start_time = datetime.now()

print(f"\nScanning started on: {target}")
print("-" * 40)

# Port Scan 1-500
for port in range(1, 501):
    thread = threading.Thread(target=scan_port, args=(target, port))
    thread.start()

print("-" * 40)
print(f"Scan completed in: {datetime.now() - start_time}")