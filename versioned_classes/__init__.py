import hashlib
import inspect
import types


def versioned_class(cls):
    """
    This decorator creates a hash of the code inside a classes method and saves it as cls.__version__
    """
    class Wrapper(cls):
        def __init__(self,*args):
            super().__init__(*args)
            m = hashlib.md5()
            for methodname, method in vars(cls).items():
                if isinstance(method, types.FunctionType):
                    m.update(inspect.getsource(method).encode("utf-8"))
            self.__version__ = m.hexdigest()
            print(self.__version__)
    return Wrapper