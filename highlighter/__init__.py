"""Flask module
file: __init__.py
date: 12.12.2012
author smith@example.com
license: MIT"""

from flask import Flask, render_template, request, Markup


def create_app():
    """Create flask app for binding."""
    app = Flask(__name__)

    template_file_name = 'index.html'

    @app.route('/', methods=['GET'])
    def index():
        return render_template(template_file_name)

    @app.route('/', methods=['POST'])
    def process():
        search_text: str = request.form['search']
        text: str = request.form['text']
        highlighted_text: str = highlight_text(text, search_text)
        result: dict = {'text': text, 'highlighted_text': Markup(highlighted_text)}
        return render_template(template_file_name, **result)

    def markup_text(text):
        """Markup given text.
        @:param text - string text to be marked
        @:return marked text, e.g., <mark>highlighted text</mark>."""

        result = '<mark>' + text + '</mark>'

        return result

    def highlight_text(text: str, expr: str):
        """Markup searched string in given text.
        @:param text - string text to be processed
        @:return marked text, e.g., "sample text <mark>highlighted part</mark> rest of the text"."""

        if expr in text:
            new_str: str = markup_text(expr)
            result = text.replace(expr, new_str)
        else:
            return "Text no found"

        return result

    return app
