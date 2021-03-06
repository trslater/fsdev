from argparse import ArgumentParser
from os import environ, stat
from pathlib import Path
from re import template

from . import fs
from .web import Server

HOST = "localhost"
PORT = 8000
PARSER = ArgumentParser(description="A simple filesystem-based dev server.")
PARSER.add_argument("command", choices=("serve", "build"),
                    help=("build outputs a static site to a build directory,"
                          "and serve starts a dev server for the site."))


def run():
    # Get environment
    root = Path(environ.get("SITE_ROOT", "."))

    # Get CLI args
    args = PARSER.parse_args()

    # Route commands
    if args.command == "serve":
        serve(root)
    
    elif args.command == "build":
        build(root)


def serve(root):
    print(f"Server started at http://{HOST}:{PORT}\n\n"
            "  Ctrl+C to exit\n")

    server = Server(HOST, PORT, root)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped.")


def build(root):
    fs.build(root)
