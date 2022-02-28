from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import mimetypes
import socket

from jinja2 import Environment, FileSystemLoader, select_autoescape, Template

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

        if mimetype in TEMPLATE_MIMETYPES:
            # Get contents from Jinja template
            env = Environment(
                loader=FileSystemLoader("templates"),
                autoescape=select_autoescape())
            template = env.get_template(f".{self.path}")
            contents = template.render().encode()
        
        # Treat everything else as a static file
        else:
            # Get contents from file
            with open(f"static{self.path}", "rb") as f:
                contents = f.read()

        # Serve contents
        self.wfile.write(contents)
    