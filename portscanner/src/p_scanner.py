#port scanner

import socket 

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

def run():
    print("=== Python Port Scanner ===")

    ip = input("Target IP: ")
    port_0 = int(input("Target Ports From: "))
    port_1 = int(input("Target Ports To: "))
    open_ports = []

    print(f"Scanning {ip}:{port_0} - {port_1}")

    for port in range(port_0, port_1 + 1):
        if scan_port(ip, port):
            open_ports.append(port)

    print("----Open Ports----")
    for port in open_ports:
        print(f"[+] {port}")
    print("------------------")