import pudb as dbg 
from django.template import Library, Node

register = Library()

class PdbNode(Node):

    def render(self, context):
        dbg.set_trace() #debugger will stop here 
        return '' 

@register.simple_tag
def pdb(parser, token):
    return PdbNode()