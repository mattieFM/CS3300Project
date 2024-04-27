from django import template
register = template.Library()
@register.simple_tag(name="iIf", takes_context=True)
def iIf(context, name, body, inverse=False):
    """A simple function for inline if, if name exists in context, return body"""
    returnVal=""
    
    if((not inverse and name in context) or (inverse and not name in context)):
        returnVal=body
        
    return returnVal
