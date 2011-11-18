from pyramid.threadlocal import get_current_request

from apex_pipeline.interfaces import IApexPipelineBlock

def add_renderer_globals(event):
    request = event.get('request')
    if request is None:
        request = get_current_request()

    blocks = request.registry.queryUtility(IApexPipelineBlock)
    
    globs = {
        'blocks': blocks.blocks,
    }
    event.update(globs)