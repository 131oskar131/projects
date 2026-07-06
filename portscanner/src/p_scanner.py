import socket
import threading
from concurrent.futures import ThreadPoolExecutor  # Manages a fixed pool of worker threads.
import time
from src.banner import banner_grabbing  # Imports the banner grabbing function.

# Prevents multiple threads from modifying shared data at the same time.
lock = threading.Lock()


# Checks whether a specific TCP port is open.
def scan_port(ip, port):
    try:
        # Creates a TCP socket that is automatically closed after use.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Maximum waiting time for a connection.
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                return True
            else:
                return False

    except Exception as e:
        return f"ERROR: {e}"


# Function executed by each worker thread.
def scan_port_thread(ip, port, open_ports):
    if scan_port(ip, port):
        # Only one thread at a time may modify the dictionary.
        with lock:
            open_ports[port] = banner_grabbing(ip, port)


# Starts the scanner.
def run():
    print("=" * 40)
    print("      PYTHON PORT SCANNER")
    print("=" * 40)

    # User input.
    ip = input("\nTarget IP: ")
    port_0 = int(input("Target Ports From: "))
    port_1 = int(input("Target Ports To: "))

    print(f"\nTarget: {ip}")
    print(f"Range: {port_0} - {port_1}")

    # Dictionary for storing open ports and their banners.
    open_ports = {}

    # Start measuring the scan time.
    start = time.time()

    print("\nScanning...\n")

    # Creates a pool with a maximum of 100 worker threads.
    with ThreadPoolExecutor(max_workers=100) as executor:

        # Submit one scanning task for every port.
        for port in range(port_0, port_1 + 1):
            executor.submit(
                scan_port_thread,
                ip,
                port,
                open_ports
            )

    # Stop measuring the scan time.
    end = time.time()

    print("\n" + "=" * 40)
    print("-" * 40)

    # Print all discovered open ports and their banners.
    for port, banner in open_ports.items():
        print(f"{port}  OPEN  {banner}")

    print("-" * 40)
    print("Scan finished.")
    print(f"in {end - start:.4f} seconds")
    print("=" * 40)
