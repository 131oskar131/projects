#port scanner

import socket 

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        sock.close()

        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"

    except Exception as e:
        return f"ERROR: {e}"

def run():
    print("=== Python Port Scanner ===")

    ip = input("Target IP: ")
    port = int(input("Target Port: "))

    print(f"Scanning {ip}:{port}")

    result = scan_port(ip, port)

    print(f"Result: {result}")