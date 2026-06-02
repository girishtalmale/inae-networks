import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# Thread 1: receive messages
def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print("\n" + msg)
        except:
            break


# Start receiver thread
threading.Thread(target=receive_messages, daemon=True).start()

# Thread 2: send messages
print("Start chatting (type 'exit' to quit)")

while True:
    msg = input()

    if msg.lower() == "exit":
        break

    client.send(msg.encode())

client.close()