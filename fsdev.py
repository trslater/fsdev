""".. include:: README.md"""

__docformat__ = "restructuredtext"

# Standard library
from pathlib import Path
import sys

# Dependencies
from bottle import abort, get, run, static_file, template

TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
MIMETYPES = {
    "css": "text/css",
    "js": "text/javascript",
    "png": "image/png",
    "jpg": "image/jpeg",
    "gif": "image/gif",
    "svg": "image/svg+xml"}
HOST = "localhost"
PORT_START = 8000
PORT_STOP = 10000


def main():
    """Main CLI entrypoint"""

    # Automatically try to find available port
    for port in range(PORT_START, PORT_STOP):
        try:
            run(host=HOST, port=port, debug=True)
            sys.exit(0)
        
        except OSError:
            continue

    else:
        print("A suitable port could not be found")
        sys.exit(1)


@get(f"/<path:path>")
@get(f"/")
def doc(path=""):
    """Route templates or static files within CWD"""

    # Strip trailing slash
    path = path.strip("/")

    # Ignore private templates
    if path and path[0] == "_":
        abort(403, "Private template.")

    try:
        extension = path.split("/")[-1].split(".")[1]

    # If no extension...
    except IndexError:
        # Treat as directory
        return template(f"{TEMPLATE_DIR}/{path}/index.html")

    # If there is an extension...
    else:
        if extension == "html":
            return template(f"{TEMPLATE_DIR}/{path}")

        elif extension in MIMETYPES.keys():
            return static_file(
                path, root=f"{STATIC_DIR}/", mimetype=MIMETYPES[extension])


if __name__ == "__main__":
    main()
