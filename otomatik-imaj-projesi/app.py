from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

APP_VERSION = os.getenv("APP_VERSION", "dev")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/live"):
            body = {
                "message": "Otomatik Docker imaj projesi calisiyor!",
                "version": APP_VERSION,
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(body, ensure_ascii=False).encode("utf-8"))
        elif self.path == "/version":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"version": APP_VERSION}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"Service starting on port {port}; APP_VERSION={APP_VERSION}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
