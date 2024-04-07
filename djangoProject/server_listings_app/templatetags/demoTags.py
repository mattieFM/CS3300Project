from django import template
import config

register = template.Library()


@register.simple_tag(name="setDemo", takes_context=True)
def checkDemo(context):
    """A function that will set isDemo to true in the context
        deprecated in v0.1
        use {% ifDemo %} content to display if demo {% endifDemo %} instead
    """
    context['isDemo'] = True


@register.tag(name='ifDemo')
def do_demo(parser, token):
    """a simple tag to only display content if demo is enabled"""
    # parse all dom nodes
    nodelist = parser.parse(("endifDemo",))
    # remove the initial demo tag
    parser.delete_first_token()
    return DemoNode(nodelist)


class DemoNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = ''
        if(config.isDemo):
            output = self.nodelist.render(context)
        return output
