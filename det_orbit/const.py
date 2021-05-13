import constantes
import sys

if constantes is None:
    class _const:
        class ConstError(TypeError):
            pass

        def __setattr__(self, name, value):
            if name in self.__dict__:
                raise self.ConstError("Can't rebind const(%s)" % name)
            self.__dict__[name] = value


    sys.modules[__name__] = _const()
