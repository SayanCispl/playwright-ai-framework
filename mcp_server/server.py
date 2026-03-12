import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Tuple


class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:  # must remain uppercase POST (required by BaseHTTPRequestHandler)
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
            user_message = data.get("messages", [])[-1].get("content", "")
        except (json.JSONDecodeError, IndexError, KeyError):
            user_message = "Invalid request"

        response = {
            "choices": [
                {
                    "message": {
                        "content": f"Mock AI Agent: Generated test cases for -> {user_message}"
                    }
                }
            ]
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def run_server() -> None:  # lowercase function name (PEP8)
    server_address: Tuple[str, int] = ("0.0.0.0", 8001)
    httpd = HTTPServer(server_address, MCPHandler)  # type: ignore
    print("MCP server running at http://0.0.0.0:8001")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
