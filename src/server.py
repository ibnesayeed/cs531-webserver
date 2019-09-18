#!/usr/bin/env python3

import socket
import sys

HOST = "localhost"
PORT = 8080

if len(sys.argv) > 1:
    HOST = sys.argv[1]
if len(sys.argv) > 2:
    PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

print(f"Listening on {HOST}:{PORT} for HTTP connectiosns\n")

while True:
    conn, addr = s.accept()
    nl = False
    he = False
    data = []
    while True:
        if he:
            break
        buf = conn.recv(1024)
        data.append(buf)
        print(f"< Reading data from the socket")
        if not buf.strip():
            print("* Empty message recieved")
            break
        for c in buf:
            if c == 13:
                pass
            elif c == 10:
                if nl:
                    he = True
                    print("* Two consecutive new lines indicate end of header")
                    break;
                nl = True
            else:
                nl = False

    payload = b"".join(data).decode()
    print(f"> Echoing back {len(payload)} bytes of request as payload\n")
    res = f"HTTP/1.1 200 OK\r\nContent-Type: message/http\r\nServer: Echo Server\r\nContent-Length: {len(payload)}\r\nConnection: close\r\n\r\n{payload}"
    conn.sendall(res.encode())
    conn.close()
