class NonlinearEquation:

    def __init__(self, fx = None, fequiv = None, to_str = None):
        self.__fx = fx
        self.__fequiv = fequiv
        self.__to_str = to_str

    def to_str(self):
        return self.__to_str

    def f(self, x):
        return self.__fx(x)

    def f_equiv(self, x):
        return self.__fequiv(x)
    