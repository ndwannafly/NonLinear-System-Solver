from methods.method import Method


class BisectionMethod(Method):
    def __init__(self, nonlinear_equation):
        self.nonlinear_equation = nonlinear_equation
    
    def execute(self):
        return self.find_root()

    def find_root(self):
        print("> Please enter your interval [a, b]: ", end = "")
        l, r = map(float, input().split())
        print("> Please enter your epsilon: ", end = "")
        self.EPS = float(input())
        
        for i in range(int(1e6)):
            m = (l + r) / 2
            fl = self.nonlinear_equation.f(l)
            fr = self.nonlinear_equation.f(r)
            fm = self.nonlinear_equation.f(m)
            if abs(fm) < self.EPS:
                l = m
                break 
            if fm * fr < 0: l = m
            elif fl * fm < 0: r = m
        
        return l if abs(self.nonlinear_equation.f(l)) < self.EPS else "There is no solution!"