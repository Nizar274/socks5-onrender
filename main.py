import socketserver
import socks

class ProxyHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(f"Incoming connection from {self.client_address}")
        # هون ما منرد ولا منعمل شي مباشر لأنه هذا SOCKS5 مش HTTP
        self.wfile.write(b"SOCKS5 Proxy is running via Render\n")

if __name__ == "__main__":
    print("Starting proxy server on port 10000...")
    with socketserver.TCPServer(("0.0.0.0", 10000), ProxyHandler) as server:
        server.serve_forever()
