#port scanner

import socket 
import threading

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
            open_ports.append(port)
        

def run():
    print("=" * 40)
    print("      PYTHON PORT SCANNER")
    print("=" * 40)

    ip = input("\nTarget IP: ")
    port_0 = int(input("Target Ports From: "))
    port_1 = int(input("Target Ports To: "))

    open_ports = []

    print(f"\nTarget: {ip}")
    print(f"Range: {port_0} - {port_1}")

    threads = []
    open_ports = []

    print("\nScanning...\n")

    for port in range(port_0, port_1 + 1):
        t = threading.Thread(
            target=scan_port_thread,
            args=(ip, port, open_ports)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n" + "-" * 40)
    print(f"Open Ports: {open_ports}")
    print("Scan finished.")
    print("-" * 40)