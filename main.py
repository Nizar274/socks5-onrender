import socket
import socks

s = socks.socksocket()
s.set_proxy(socks.SOCKS5, "127.0.0.1", 1080)
s.bind(("0.0.0.0", 1080))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("Connection from", addr)
