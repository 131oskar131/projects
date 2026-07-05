#port scanner

import socket 
import threading
from concurrent.futures import ThreadPoolExecutor
import time
from src.banner import banner_grabbing

lock = threading.Lock()

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                return True
            else:
                return False

    except Exception as e:
        return f"ERROR: {e}"

def scan_port_thread(ip, port, open_ports):
    if scan_port(ip, port):
        with lock:
            open_ports[port] = banner_grabbing(ip, port)

        

def run():
    print("=" * 40)
    print("      PYTHON PORT SCANNER")
    print("=" * 40)

    ip = input("\nTarget IP: ")
    port_0 = int(input("Target Ports From: "))
    port_1 = int(input("Target Ports To: "))

    print(f"\nTarget: {ip}")
    print(f"Range: {port_0} - {port_1}")
    open_ports = {}

    start = time.time()
    print("\nScanning...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:

        for port in range(port_0, port_1 + 1):
            executor.submit(
                scan_port_thread,
                ip,
                port,
                open_ports
            )

    end = time.time()

    print("\n" + "=" * 40)
    print("-" * 40)
    for port, banner in open_ports.items():
        print(f"{port}  OPEN  {banner}")
    print("-" * 40)
    print("Scan finished.")
    print(f"in {end - start:.4f} seconds")
    print("=" * 40)