from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HABITS = [
    {"id": 1, "name": "Drink water", "done_today": False},
    {"id": 2, "name": "Morning exercise", "done_today": True},
    {"id": 3, "name": "Read 20 minutes", "done_today": False},
]


class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {"status": "ok"})
        elif self.path == "/habits":
            self.send_json(200, HABITS)
        else:
            self.send_json(404, {"error": "not found"})


if __name__ == "__main__":
    print("Habit tracker API started on port 8080", flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
