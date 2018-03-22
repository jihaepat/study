
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes('hellow','utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler)
    print('Started WebServer on port 8888...')
    print('Press ^C to quit WebServer')
    server.serve_forever()
