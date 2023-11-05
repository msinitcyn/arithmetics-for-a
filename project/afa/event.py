class Event:
    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        self.handlers.append(handler)

    def unsubscribe(self, handler):
        self.handlers.remove(handler)

    def __iadd__(self, handler):
        self.handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self

    def __call__(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)

