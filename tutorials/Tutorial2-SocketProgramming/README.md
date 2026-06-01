# Socket Programming Lab

> **Note:** The Jupyter Notebook (`socket_programming_lab.ipynb`) is identical for **Windows, Linux, and macOS**. The instructions and code examples work the same across all three operating systems unless otherwise noted.



## Objective

This lab introduces the basics of **socket programming** using Python. Students will learn how two applications communicate over a network using sockets and understand the differences between TCP and UDP communication.

Although example implementations for both TCP and UDP are provided, **only the UDP implementation will be used during the lab session.**

## Before You Start

Please go through the references provided in this repository and inside the notebook before starting the exercises. Understanding the basic concepts of:

* Client and Server architecture
* IP addresses and Port numbers
* TCP vs UDP communication
* Socket APIs in Python

will make the lab significantly easier to follow.

## Installation

Python 3.8+ is recommended.

Check your Python installation:

```bash
python --version
```

No external packages are required for the socket examples. The `socket` module is part of Python's standard library.

You can verify it by running:

```bash
python -c "import socket; print('Socket module available')"
```

## Python Files Overview

The folder contains small Python examples that demonstrate socket programming with UDP and TCP.

### UDP Client and Server

* `UDP_server.py` starts a UDP server on port `5000`. It waits for messages from clients and sends a response back to the sender.
* `UDP_client.py` sends a fixed list of messages to the UDP server and prints the server responses.
* `UDP_chat_client.py` is an interactive UDP client. You can type messages manually and receive responses from `UDP_server.py`.

UDP is connectionless, so the client sends each message directly without creating a long-running connection first.

### TCP Client and Server

* `TCP_server.py` starts a simple TCP server on `127.0.0.1:1234`. It accepts a connection, receives one message, sends a response, and closes that client connection.
* `TCP_echo_server.py` starts a threaded TCP echo server on `127.0.0.1:1235`. It can handle multiple clients and echoes received messages back.
* `TCP_client.py` connects to `127.0.0.1:1235`, sends multiple messages, and prints the responses. This file is intended to run with `TCP_echo_server.py`.
* `TCP_chat_server.py` starts a multi-client TCP chat server on port `1234`.
* `TCP_chat_client.py` connects to the TCP chat server and lets a user type chat messages interactively.

TCP is connection-oriented, so the client connects to the server before sending messages.

## Running the Programs

### Terminal Usage

Socket programs require multiple processes running simultaneously.

Open **two terminal windows**:

### Run the UDP Example

#### Terminal 1 (Server)

```bash
python UDP_server.py
```

#### Terminal 2 (Client)

```bash
python UDP_client.py
```

The server should be started first so that it is ready to receive messages from the client.

To use the interactive UDP client instead:

```bash
python UDP_chat_client.py
```

### Run the TCP Echo Example

TCP examples are also included for reference:

#### Terminal 1 (Server)

```bash
python TCP_echo_server.py
```

#### Terminal 2 (Client)

```bash
python TCP_client.py
```

### Run the TCP Chat Example

#### Terminal 1 (Server)

```bash
python TCP_chat_server.py
```

#### Terminal 2 and More (Clients)

```bash
python TCP_chat_client.py
```

However, these are provided primarily for comparison and are **not used in the lab exercises**.

## Important Socket Functions

During the lab, pay attention to the following commonly used APIs:

```python
socket.socket()
```

Creates a socket object.

```python
sock.bind()
```

Associates a socket with a local IP address and port.

```python
sock.sendto()
```

Sends data using UDP.

```python
sock.recvfrom()
```

Receives data using UDP.

## Recommended Learning Resources

### Beginner-Friendly Resources

1. Python Socket Programming Tutorial
   https://realpython.com/python-sockets/

2. Python Socket Programming (GeeksforGeeks)
   https://www.geeksforgeeks.org/python/socket-programming-python/

3. Socket Programming HOWTO (Python Documentation)
   https://docs.python.org/3/howto/sockets.html

4. Network Programming with Python (TutorialsPoint)
   https://www.tutorialspoint.com/python/python_networking.htm

### UDP-Specific References

1. UDP Client-Server Concepts (GeeksforGeeks)
   https://www.geeksforgeeks.org/computer-networks/udp-client-server-using-connect-c-implementation/

2. Python UDP Socket Example
   https://pythontic.com/modules/socket/udp-client-server-example

## Suggested Learning Order

1. Read the notebook.
2. Understand client-server communication.
3. Study the UDP examples.
4. Run the UDP server and client in separate terminals.
5. Experiment by modifying messages and port numbers.
6. Compare the UDP implementation with the TCP implementation.

---

**Author:** `Mayank` with the assistance of `ChatGPT` and `Codex`
