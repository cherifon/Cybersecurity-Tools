import socket

def port_scanner(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object: AF_INET for IPv4, SOCK_STREAM for TCP
        socket.setdefaulttimeout(1) # Set the timeout to 1 second to speed up the scanning process
        result = sock.connect_ex((target, port)) # Return 0 if the port is open, otherwise return an error code
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__": 
    target = input("Enter the target IP address: ")
    ports = [int(port) for port in input("Enter the ports to scan (separated by space): ").split()]
    port_scanner(target, ports)
