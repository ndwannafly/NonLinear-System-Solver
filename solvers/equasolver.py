from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from methods.bisection import BisectionMethod
from methods.equaiteration import EquationIterationMethod
from solvers.solver import Solver


class EquationSolver(Solver):
    DASH = '-' * 10
    SCALE = 6


    def __init__(self, equations):
        self.equations = equations
    
    
    def execute(self):
        print("> Please choose one of the equations below")
        for i, equation in enumerate(self.equations):
            if (i < 3): print("> {}. {}".format(i, equation.to_str()))
        print("> Enter your choice: ", end="")
        option = int(input())
        self.write_ans(self.iteration_solver(option))
        self.write_ans(self.bisection_solver(option))


    def iteration_solver(self, option):
        iteration = EquationIterationMethod(self.equations[option])
        return self.solving(iteration, "SIMPLE ITERATION METHOD", option)
    
    def bisection_solver(self, option):
        bisection = BisectionMethod(self.equations[option])
        return self.solving(bisection, "BISECTION METHOD", option)

    def solving(self, method, name, option):
        print("> {} {} {}".format(self.DASH, name, self.DASH))
        ans = 0
        try:
            ans = method.execute()
            ans = round(ans, self.SCALE)
        except:
            ans = "There is no solutions!"
        
        return ans

    def write_ans(self, ans):
        if (isinstance(ans, float)):
            print("> The solution of this equation is: {}".format(ans))
        else:
            print("> {}".format(ans))
