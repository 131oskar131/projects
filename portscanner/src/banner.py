import socket 

def banner_grabbing(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            
            sock.connect((ip, port))

            banner = sock.recv(1024)

            banner = banner.decode()

            return banner
        
    except Exception as e:
        return ""