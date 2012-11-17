from django import template

register = template.Library()

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


 
#class SetVarNode(template.Node):
# 
#    def __init__(self, var_name, var_value):
#        self.var_name = var_name
#        self.var_value = var_value
# 
#    def render(self, context):
#        try:
#            value = template.Variable(self.var_value).resolve(context)
#        except template.VariableDoesNotExist:
#            value = ""
#        context[0][self.var_name] = value
#        return u""
# 
#def set_var(parser, token):
#    """
#        {% set <var_name>  = <var_value> %}
#    """
#    parts = token.split_contents()
#    if len(parts) < 4:
#        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
#    return SetVarNode(parts[1], parts[3])
# 
#register.tag('set', set_var)

from django import template

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