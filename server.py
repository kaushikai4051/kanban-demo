import http.server
import webbrowser
import os

PORT = 8080
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} — {fmt % args}")

if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"Kanban board running at {url}")
        print("Press Ctrl+C to stop.\n")
        webbrowser.open(url)
        httpd.serve_forever()
