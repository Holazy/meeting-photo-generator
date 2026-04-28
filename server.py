from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

import os
os.chdir(r"e:\【09】AI\会议合照")
server = HTTPServer(('localhost', 8888), CORSHTTPRequestHandler)
print("Server started at http://localhost:8888")
server.serve_forever()
