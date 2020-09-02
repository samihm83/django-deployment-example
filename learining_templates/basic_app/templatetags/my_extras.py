from django import template

register = template.Library()

@register.filter(name='cu')
def cut(value,arg):
    """
    This cuts out all value of "arg" from the string!

    """
    return value.replace(arg,'')


# register.filter('cu',cut)
