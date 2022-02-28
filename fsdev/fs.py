"""Filesystem handling"""

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path


def read(filename, is_template, template_dir, static_dir):
    if is_template:
        # Get contents from Jinja template
        env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape())
        template = env.get_template(filename)
        return template.render()
    
    # Treat everything else as a static file
    with open(static_dir/filename, "r") as f:
        return f.read()
