import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)

server_ip = "127.0.0.1"
server_port = 5000

print("UDP Echo Client Started")
print("Type 'exit' to quit\n")

while True:
    message = input("Enter message: ")

    if message.lower() == "exit":
        print("Closing client...")
        break

    # Send message to server
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Receive echo response
    try:
        response, server_addr = client_socket.recvfrom(1024)
        print("Server Response:", response.decode())
    except socket.timeout:
        print("No response from server (timeout)")

client_socket.close()