import socket

HOST = "127.0.0.1"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

print(f"TCP Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_addr = server.accept()

    print(f"Connection from {client_addr}")

    data = client_socket.recv(1024)

    print("Received:", data.decode())

    response = f"Message received : {data.decode()}"
    client_socket.send(response.encode())

    client_socket.close()