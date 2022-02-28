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
    src_dir = Path(environ.get("SRC_DIR", "."))

    # Get CLI args
    args = PARSER.parse_args()

    template_dir = src_dir/"templates"
    static_dir = src_dir/"static"

    # Route commands
    if args.command == "serve":
        serve(template_dir, static_dir)
    
    elif args.command == "build":
        build(template_dir, static_dir)


def serve(template_dir, static_dir):
    print(f"Server started at http://{HOST}:{PORT}\n\n"
            "  Ctrl+C to exit\n")

    server = Server(HOST, PORT, template_dir, static_dir)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped.")


def build(template_dir, static_dir):
    fs.build(template_dir, static_dir)
