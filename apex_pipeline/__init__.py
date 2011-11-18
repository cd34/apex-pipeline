from apex_pipeline.directives import add_block

def includeme(config):
    config.add_static_view('apex_pipeline/static', 'apex_pipeline:static')

    config.add_directive('add_block', add_block)

    #config.add_page('package.pages.index', route_name='index', blocks=['#content', '#top'])
    #config.add_subscriber('apex_pipeline.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')