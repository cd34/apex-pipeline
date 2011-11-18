from pyramid.compat import string_types
from pyramid.exceptions import ConfigurationError

from apex_pipeline.interfaces import IApexPipelineBlock
from apex_pipeline.interfaces import Blocks

def add_block(config, block, name=None, identified_by=None, weight=0):    
    registry = config.registry
    dotted = config.maybe_dotted
    
    if not isinstance(block, string_types):
        raise ConfigurationError(
            'The "block" argument to add_block must be a '
            'dotted name to a globally importable object, not %r' %
            block)
            
    if identified_by[0] not in ['.', '#']:
        raise ConfigurationError(
            'The "identified_by" argument to add_block must'
            'start with a "." or "#".'
        )

    block = dotted(block)
    
    blocks = registry.queryUtility(IApexPipelineBlock)
    if blocks is None:
        blocks = Blocks()
        registry.registerUtility(blocks, IApexPipelineBlock)
        blocks.add(identified_by, block)

    def register():
        blocks.add(identified_by, block)

    config.action(('pipeline_block', block, identified_by), register)

    return block    
