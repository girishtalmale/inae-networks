import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)

server_ip = "127.0.0.1"
server_port = 5000

messages = ["Hello UDP Server",
            "This is my second message to you",
            "Do we have a three way handshake",
            "I guess not, we are UDP",
            "TCP makes a three way  handshake for a connection",
            "Slow to talk a word"]
# Sending Multiple Messages
for message in messages:

    # Send data
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Receive response
    try:
        response, server_addr = client_socket.recvfrom(1024)
        print("Server Response:", response.decode())
    except socket.timeout:
        print("No response from server.")

client_socket.close()