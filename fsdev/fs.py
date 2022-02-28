"""Filesystem handling"""

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path


def read(root, path):
    env = Environment(
        loader=FileSystemLoader((root)),
        autoescape=select_autoescape())
    template = env.get_template(str(path))
    return template.render()


def build(root):
    raise NotImplemented()
