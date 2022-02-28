from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import mimetypes

from . import fs

TEMPLATE_MIMETYPES = ("text/html",)


class Server(ThreadingHTTPServer):
    """A simple extension of the built-in `ThreadingHTTPServer` to always use the same
    handler."""

    def __init__(self, host: str, port: int) -> None:
        super().__init__((host, port), Handler)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Assume everything works
        self.send_response(200)

        # Handle indexes
        self.path += "index.html" if self.path[-1] == "/" else ""

        # Discover and set appropriate MIME type
        mimetype, _ = mimetypes.guess_type(self.path)
        self.send_header("Content-type", mimetype)
        self.end_headers()

        is_template = mimetype in TEMPLATE_MIMETYPES

        contents = fs.read(self.path, is_template)

        # Serve contents
        self.wfile.write(contents.encode())
    