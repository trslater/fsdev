from .server import Server

HOST = "localhost"
PORT = 8000


def run():
    print(f"Server started at http://{HOST}:{PORT}\n\n"
          "  Ctrl+C to exit\n")

    server = Server(HOST, PORT)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped.")
