""".. include:: README.md"""

__docformat__ = "restructuredtext"

# Standard library
import os
from pathlib import Path
import sys

# Dependencies
import flask
from flask import Flask

MIMETYPES = {
    "css": "text/css",
    "js": "text/javascript",
    "png": "image/png",
    "jpg": "image/jpeg",
    "gif": "image/gif",
    "svg": "image/svg+xml"}

APP = Flask(__name__,
            template_folder=f"{os.getcwd()}/templates",
            static_folder=f"{os.getcwd()}/static")


@APP.get(f"/<path:path>")
@APP.get(f"/")
def doc(path=""):
    """Route templates or static files within CWD"""

    # Strip trailing slash
    path = path.strip("/")

    # Ignore private templates
    if path and path[0] == "_":
        flask.abort(403, "Private template.")

    try:
        extension = path.split("/")[-1].split(".")[1]

    # If no extension...
    except IndexError:
        # Treat as directory
        return flask.render_template(f"{path}/index.html")

    # If there is an extension...
    else:
        if extension == "html":
            return flask.render_template(f"{path}")

        elif extension in MIMETYPES.keys():
            return flask.send_from_directory(APP.static_folder, path,
                                             mimetype=MIMETYPES[extension])
