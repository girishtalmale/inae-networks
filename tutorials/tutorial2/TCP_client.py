import socket

HOST = "127.0.0.1"
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(10)
client.connect((HOST, PORT))

messages = ["Hello TCP Server",
            "This is my second message to you",
            "Do we have a three way handshake",
            "Yes , we are TCP",
            "TCP makes a three way  handshake for a connection",
            "Slow to talk a word"]

for message in messages:

    # Send data
    client.sendto(message.encode(), (HOST, PORT))

    # Receive response
    try:
        response, server_addr = client.recvfrom(1024)
        print("Server Response:", response.decode())
    except socket.timeout:
        print("No response from server.")

client.close()