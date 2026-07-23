from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
import json
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'ok',
                'mode': 'local-dev',
                'message': 'Local dynamic API is ready.'
            }).encode())
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == '/api/interpret':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8') if length else '{}'
            payload = json.loads(body or '{}')
            response = {
                'received': True,
                'module': payload.get('module', 'unknown'),
                'message': 'Local dynamic analysis accepted.',
                'timestamp': 'local-dev'
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            return
        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    server = ThreadingHTTPServer(('127.0.0.1', 8000), Handler)
    print('Serving on http://127.0.0.1:8000')
    server.serve_forever()
