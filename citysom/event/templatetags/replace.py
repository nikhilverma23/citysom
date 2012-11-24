from django import template

register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


class AssignNode(template.Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def render(self, context):
        context[self.name] = self.value.resolve(context, True)
        return ''

def do_assign(parser, token):
    """
    Assign an expression to a variable in the current context.
    
    Syntax::
        {% assign [name] [value] %}
    Example::
        {% assign list entry.get_related %}
        
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError("'%s' tag takes two arguments" % bits[0])
    value = parser.compile_filter(bits[2])
    return AssignNode(bits[1], value)

register = template.Library()
register.tag('assign', do_assign)

from django import template
register = template.Library()

@register.filter
def keyvalue(dict, key):    
    return dict[key]