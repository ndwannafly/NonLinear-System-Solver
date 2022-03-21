import random
from methods.method import Method


class EquationIterationMethod(Method):
    def __init__(self, nonlinear_equation):
        self.__nonlinear_equation = nonlinear_equation

    def execute(self):
        return self.find_root()

    def find_root(self):
        print("> please enter your interval [a, b]: ", end = "")
        a, b = map(float, input().split())
        print("> Please enter your epsilon: ", end = "")
        self.EPS = float(input())
        x1 = random.random() * (b - a) + a
        prv_val = -1e9
        for iter in range(int(1e6)):
            if abs(self.__nonlinear_equation.f(x1)) < self.EPS and abs(prv_val - x1) < self.EPS:
                return x1
            if (x1.real < a or x1.real > b): return "There is no solution!!"
            x1 = self.__nonlinear_equation.f_equiv(x1)

        
        return x1 if abs(self.__nonlinear_equation.f(x1)) < self.EPS else "There is no solution!"