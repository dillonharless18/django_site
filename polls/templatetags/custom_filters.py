# Cannot use some functionality of Python directly in Views Django
# Therefore I created a filter to explore that functionality

from django import template

register = template.Library()

@register.filter
def reverse_string(value):
    return value[::-1]
