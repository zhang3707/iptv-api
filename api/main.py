import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # 读取你生成的 m3u 文件并返回
        file_path = os.path.join(os.path.dirname(__file__), '../output/user_result.m3u')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            self.wfile.write("TV file not found yet.".encode('utf-8'))
        return
