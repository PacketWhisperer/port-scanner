import socket

# Function to scan a port
def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[OPEN] Port {port}")
        sock.close()
    except:
        print(f"[CLOSED] Port {port}")

# Get user input
target_ip = input("Enter the IP address to scan: ")

# Scan ports 20 to 1024
print(f"Scanning ports on {target_ip}...")
for port in range(20, 1025):
    scan_port(target_ip, port)