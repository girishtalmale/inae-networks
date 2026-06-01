import socket
import threading

HOST = "0.0.0.0"
PORT = 1234

clients = []
clients_lock = threading.Lock()


def broadcast(message, sender_conn=None):
    with clients_lock:
        for client in clients:
            if client != sender_conn:
                try:
                    client.send(message.encode())
                except:
                    pass


def handle_client(conn, client_addr):
    print(f"New connection from {client_addr}")

    with clients_lock:
        clients.append(conn)

    try:
        conn.send("Welcome to the chat!\n".encode())

        while True:
            data = conn.recv(1024)

            if not data:
                break

            message = data.decode().strip()

            print(f"[{client_addr}] {message}")

            broadcast(
                f"{client_addr[0]}:{client_addr[1]} says: {message}",
                conn
            )

    finally:
        print(f"Client {client_addr} disconnected.")

        with clients_lock:
            if conn in clients:
                clients.remove(conn)

        conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(10)

print(f"Chat Server listening on {HOST}:{PORT}")

while True:
    conn, client_addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, client_addr),
        daemon=True
    )

    thread.start()