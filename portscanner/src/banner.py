import socket 

# function for banner grabbing process
def banner_grabbing(ip, port):
    try:
        # Creates a TCP socket that is automatically closed after use.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Maximum waiting time for a connection.
            sock.settimeout(2)
            
            sock.connect((ip, port))

            banner = sock.recv(1024)

            banner = banner.decode()

            return banner
        
    except Exception as e:
        # returns nothing for now but will be changed
        return ""
