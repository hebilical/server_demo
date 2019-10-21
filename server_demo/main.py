
import os
import importlib
from tornado.web import Application
from tornado.ioloop import IOLoop
# import server_demo.view.demo as demo_view




def server_handle(io_loop=None):
    views_list = []
    module = importlib.import_module('.', 'server_demo.view')
    views = os.listdir(module.__dict__['__path__'][0])
    views_list = []
    for i in views:
        if   i.startswith('__') is False:
            view_module = importlib.import_module('.', f'server_demo.view.{i[:-3]}')
            view_md = view_module.__dict__
            views_item_list = [
                view_md[c] for c in view_md if (
                    isinstance(view_md[c], type) and view_md[c].__module__ == view_module.__name__
                )]
            views_list.extend(views_item_list)
    route_list = [(j.route, j) for j in views_list]
    app =  Application(route_list)
    app.listen(os.environ.get('PORT', 8000))
    if io_loop is None:
        io_loop = IOLoop.current()
    io_loop.start()
