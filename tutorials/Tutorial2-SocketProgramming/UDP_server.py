import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to IP and port
server_socket.bind(("0.0.0.0", 5000))

print("UDP Server listening on port 5000...")

while True:
    # Receive data
    data, client_addr = server_socket.recvfrom(1024)

    message = data.decode()

    print(f"Received from {client_addr}: {message}")

    # Send response
    response = f"Server received: {message}"

    server_socket.sendto(response.encode(), client_addr)