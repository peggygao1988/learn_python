def singleton(cls):
    instances = {}

    def wraps(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return wraps


@singleton
class C1(object):
    pass

if __name__ == '__main__':
    a = C1()
    b = C1()
    a is b
