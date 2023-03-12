from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut (value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    # the replace method is a stirng method that will replace what you are looking for with what you want 
    # to replace it with, in this case an empty string
    return value.replace(arg, '')

