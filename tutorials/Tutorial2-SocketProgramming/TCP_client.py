import socket

HOST = "127.0.0.1"
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = "Hello Server"

client.send(message.encode())

response = client.recv(1024)

print("Server replied:", response.decode())

client.close()