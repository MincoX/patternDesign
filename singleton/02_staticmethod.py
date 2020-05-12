import threading


class SessionManager:
    """
    线程锁控制并发时刻只有一个实例创建，但是同步代码部分效率低下
    """
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs) -> None:
        self.name = kwargs.get('name')

    @classmethod
    def instance(cls, *args, **kwargs):
        with SessionManager._instance_lock:
            if not hasattr(cls, '_instance'):
                cls._instance = cls(*args, **kwargs)

        return cls._instance


class SessionManager:
    """
    双重判断，一旦成功创建实例后就不会再出现阻塞的情况，提高效率
    """
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs) -> None:
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SessionManager._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = cls(*args, **kwargs)

        return cls._instance


if __name__ == '__main__':
    session = SessionManager(*(), **{})
    sin = SessionManager.instance(*(), **{'name': 'MincoX'})
    sin1 = SessionManager.instance(*(), **{})

    print(sin == sin1, type(sin) == type(sin1), id(sin) == id(sin1))
