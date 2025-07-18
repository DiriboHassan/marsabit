from django import template

register = template.Library()

@register.filter
def replace(value, arg):
    """Replace all occurrences of a substring in a string."""
    old, new = arg.split(',')
    return value.replace(old, new)