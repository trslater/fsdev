"""Filesystem handling"""

from jinja2 import Environment, FileSystemLoader, select_autoescape


def read(filename, is_template):
    if is_template:
        # Get contents from Jinja template
        env = Environment(
            loader=FileSystemLoader("templates"),
            autoescape=select_autoescape())
        template = env.get_template(f".{filename}")
        return template.render()
    
    # Treat everything else as a static file
    with open(f"static{filename}", "r") as f:
        return f.read()
