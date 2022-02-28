"""Filesystem handling"""

import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path


def read(root, path):
    env = Environment(
        loader=FileSystemLoader((root)),
        autoescape=select_autoescape())
    template = env.get_template(str(path))
    return template.render()


def build(root):
    build_dir = Path("build")

    directories = [root]

    while directories:
        directory = directories.pop()
        
        with os.scandir(directory) as scanner:
            for entry in scanner:
                if entry.is_dir():
                    directories.append(entry)
                
                elif entry.is_file():
                    if entry.name[0] == "_":
                        continue

                    rel_path = entry.path.replace(f"{root}/", "")
                    output_path = build_dir/rel_path

                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    with output_path.open("w+") as f:
                        f.write(read(root, rel_path))
