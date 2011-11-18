from zope.interface import Interface
from zope.interface import implementer

class IApexPipelineBlock(Interface):
    """ Pipeline Block Interface.
    """
    
@implementer(IApexPipelineBlock)
class Blocks(object):
    def __init__(self):
        self.blocks = []
        self.identifiers = []

    def add(self, identified_by, block):
        if identified_by not in self.identifiers:
            self.blocks.append((identified_by, block()))
            self.identifiers.append(identified_by)

    def __call__(self, handler, registry):
        for identified_by, block in self.blocks:
            handler = block(handler, registry)
        return handler