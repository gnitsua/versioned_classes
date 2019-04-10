import hashlib
import inspect


def versioned_class(cls):
    m = hashlib.md5()
    for methodname, method in inspect.getmembers(cls):
        if inspect.ismethod(method):
            m.update(inspect.getsource(method).encode("utf-8"))
    cls.__version__ = m.hexdigest()
    return cls