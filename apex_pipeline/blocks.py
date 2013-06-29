"""
    served via: esi, javascript, asyncjs, socketo

    header block: add js includes
    footer block:
"""
class Block(object):
    def __init__(self, **kw):
        self.esi = kw.get('esi', False)

class BlockESI(Block):
    def __init__(self, **kw):
        esi = True
