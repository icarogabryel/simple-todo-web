from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            with open(f'../frontend/index.html', 'r') as html:
                self.wfile.write(html.read().encode('utf-8'))

        elif self.path == '/style.css':
            self.send_response(200)
            self.send_header('Content-Type', 'text/css')
            self.end_headers()
            
            with open(f'../frontend/style.css', 'r') as css:
                self.wfile.write(css.read().encode('utf-8'))
                
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found: The requested path does not exist.')

if __name__ == '__main__':
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port 8080...')
    httpd.serve_forever()
