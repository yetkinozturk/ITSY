from django import template
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import guess_lexer_for_filename, TextLexer
from pygments.util import ClassNotFound

register = template.Library()

@register.filter('highlight')
def highlight_filter(text, filename):
    try:
        lexer = guess_lexer_for_filename(filename, text)
    except ClassNotFound:
        lexer = TextLexer()

    return mark_safe(highlight(
        text,
        lexer,
        HtmlFormatter(linenos="table", lineanchors="line")
    ))


@register.simple_tag
def highlight_css():
    return HtmlFormatter(linenos="table", lineanchors="line").get_style_defs()
