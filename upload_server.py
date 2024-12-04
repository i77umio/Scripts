from http.server import SimpleHTTPRequestHandler, HTTPServer
import argparse

class CustomHandler(SimpleHTTPRequestHandler):
    def do_PUT(self):
        path = self.translate_path(self.path)
        content_length = int(self.headers['Content-Length'])
        with open(path, 'wb') as output_file:
            output_file.write(self.rfile.read(content_length))
        self.send_response(200, "File uploaded successfully!")
        self.end_headers()

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Custom HTTP server with PUT support.")
    parser.add_argument("--port", type=int, default=8000, help="Port number to listen on (default: 8000)")
    args = parser.parse_args()

    # Use the specified port
    server_address = ("", args.port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Serving on port {args.port}...")
    httpd.serve_forever()
