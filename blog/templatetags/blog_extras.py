from atexit import register
from glob import escape
from sys import prefix
from django import template
from django.template.defaultfilters import stringfilter
# from django.contrib.auth.admin import U
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()

@register.filter(name="cut")
@stringfilter
def cut(value, args):
    return value.replace(args, '')

@register.filter(name="lower")
@stringfilter
def lower(value):
    return value.lower()

@register.filter(name="upper")
@stringfilter
def upper(value):
    return value.upper()

@register.filter
def author_deital(author):
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)


@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">'.format(extra_classes))

@register.simple_tag
def endrow():
    return format_html('</div>')

@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context['request']
    current_user = request.user
    post = context['post']
    author = post.author
    if current_user == author:
        return format_html('<strong>Me</strong>')
    
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
    