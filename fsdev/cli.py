from argparse import ArgumentParser

from .web import Server

HOST = "localhost"
PORT = 8000
PARSER = ArgumentParser(description="A simple filesystem-based dev server.")
PARSER.add_argument("command", choices=("serve", "build"),
                    help=("build outputs a static site to a build directory,"
                          "and serve starts a dev server for the site."))


def run():
    args = PARSER.parse_args()

    if args.command == "serve":
        serve()
    
    elif args.command == "build":
        build()


def serve():
    print(f"Server started at http://{HOST}:{PORT}\n\n"
            "  Ctrl+C to exit\n")

    server = Server(HOST, PORT)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped.")


def build():
    raise NotImplemented()
