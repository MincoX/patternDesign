import threading


class SessionManager(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        self.name = kwargs.get('name')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SessionManager._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)

        return cls._instance


if __name__ == '__main__':
    # session = SessionManager(*(), **{})
    sin = SessionManager(*(), **{'name': 'MincoX'})
    # sin1 = SessionManager(*(), **{})
    print(sin.name)

    # print(sin == sin1, type(sin) == type(sin1), id(sin) == id(sin1))
