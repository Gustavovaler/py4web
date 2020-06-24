from quik import FileLoader

def render(template, context):    

    loader = FileLoader('public/views/')
    template = loader.load_template(template)
    return template.render(context,
                          loader=loader).encode('utf-8')


