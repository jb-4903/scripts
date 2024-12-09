import socket

def scan_ports(ip, start_port, end_port):
    """Scan and print open ports on the given IP address."""
    try:
        print(f"Scanning {ip} for open ports from {start_port} to {end_port}...\n")
        open_ports = []

        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Set a timeout for the connection attempt
                result = sock.connect_ex((ip, port))  # Attempt to connect to the port
                if result == 0:  # Port is open
                    open_ports.append(port)
                    print(f"Port {port} is open.")

        if not open_ports:
            print("\nNo open ports found.")
        else:
            print(f"\nOpen ports on {ip}: {open_ports}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # User input for target IP and port range
    target_ip = input("Enter the target IP address: ").strip()
    try:
        start = int(input("Enter the starting port number: ").strip())
        end = int(input("Enter the ending port number: ").strip())
        if start <= 0 or end > 65535 or start > end:
            print("Invalid port range. Ports must be between 1 and 65535, and the start port should be less than or equal to the end port.")
        else:
            scan_ports(target_ip, start, end)
    except ValueError:
        print("Invalid input. Please enter valid numbers for ports.")

input("")
