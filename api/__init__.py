from simpletor import application
from settings import pass_code
import tornado

class Api():
    def __init__(self, auth=False):
        self.auth = auth

    def __call__(self, method):
        def __method(handler, *args, **kwds):

            try:
                method(handler, *args, **kwds)
            except application.AppError as e:
                handler.set_status(400)
                handler.render_json(dict(message=e.value))

        return __method