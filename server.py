#!/usr/bin/env python3

import socket

HOST = "0.0.0.0"
PORT = 8888

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
    req = conn.recv(1024)
    print(req)
    conn.sendall(res.encode("utf-8"))
    conn.close()
