import wrapt


class Canvas(object):
    def __init__(self, *args, **kwargs):
        pass

    def image(self, w, h, uri):
        print('canvas.image ', w, h, uri)


@wrapt.decorator
def app(wrapped, instance, args, kwargs):
    return wrapped(*args, **kwargs)