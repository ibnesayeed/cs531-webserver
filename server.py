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

print("Listening on {}:{} for HTTP connectiosns".format(HOST, PORT))

res = """\
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 14
Connection: close

Hello, World!
"""

while True:
    conn, addr = s.accept()
    while True:
        req = conn.recv(1024)
        print(req)
        if req.strip() == b"":
            break
    conn.sendall(res.encode("utf-8"))
    conn.close()
