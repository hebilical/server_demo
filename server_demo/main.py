
import os
import importlib
from tornado.web import Application
from tornado.ioloop import IOLoop
# import server_demo.view.demo as demo_view




def server_handle(io_loop=None):
    views_list = []
    module = importlib.import_module('.', 'server_demo.view.demo')
    md = module.__dict__
    views_list = [
        md[c] for c in md if (
            isinstance(md[c], type) and md[c].__module__ == module.__name__
        )
    ]

    route_list = [(i.route, i) for i in views_list]

    app =  Application(route_list)
    app.listen(os.environ.get('PORT', 8000))
    if io_loop is None:
        io_loop = IOLoop.current()
    io_loop.start()

if __name__ == '__main__':
    server_handle()
