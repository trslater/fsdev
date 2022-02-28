# fsdev

A super simple filesystem dev server.

## Usage

Absolutely zero configuration. Just type `fsdev` in the directory you want to serve. Static files go in `static` and templates go in `templates`. You can make templates *private* (hide from server) by prepending with an underscore (e.g., `_header.html`). This is great for partials.

## Known Issues

-   Import warning on serve

## Documentation

Documentation in Markdown. Configured to use pdoc documentation tool:

```
poetry run pdoc fsdev.py
```
