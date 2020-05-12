def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)

        return _instance[cls]

    return _singleton


@singleton
class SessionManager:

    def __init__(self, *args, **kwargs) -> None:
        pass


if __name__ == '__main__':
    session = SessionManager(*(), **{})
    sin = SessionManager(*(), **{})
    sin1 = SessionManager(*(), **{})
    print(sin == sin1, type(sin) == type(sin1), id(sin) == id(sin1))
