from django import template
from testapp import functions


register = template.Library()

@register.filter
def filter_drive_url(value):
    return functions.get_drive_url(value)
    
@register.filter
def pre_attach(value,arg):
    return arg+str(value)