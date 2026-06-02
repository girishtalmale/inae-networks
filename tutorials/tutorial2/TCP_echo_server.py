import socket
import threading

HOST = "127.0.0.1"
PORT = 1235


def handle_client(client_socket, client_addr):
    print(f"Connection from {client_addr}")

    with client_socket:
        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode()
            print(f"[{client_addr}] {message}")

            response = f"Echo: {message}"
            client_socket.send(response.encode())

    print(f"Client {client_addr} disconnected")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print(f"TCP Server listening on {HOST}:{PORT}")

while True:
    client_socket, client_addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_addr),
        daemon=True
    )
    thread.start()