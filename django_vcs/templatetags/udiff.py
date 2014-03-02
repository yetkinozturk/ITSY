from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from django_vcs.diff import prepare_udiff

register = template.Library()

@register.filter
def render_diff(text):
    diffs, info = prepare_udiff(text)
    return render_to_string('django_vcs/udiff.html', {'diffs': diffs, 'info': info})

@register.inclusion_tag('django_vcs/diff_css.html')
def diff_css():
    return {}
