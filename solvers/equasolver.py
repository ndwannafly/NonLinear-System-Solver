from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from methods.bisection import BisectionMethod
from methods.equaiteration import EquationIterationMethod
from solvers.solver import Solver


class EquationSolver(Solver):
    DASH = '-' * 10
    SCALE = 6
    fig, axes = plt.subplots(2)
    fig_num = 0


    def __init__(self, equations):
        self.equations = equations

    def reset(self):
        self.fig_num = 0
        self.fi, self.axes = plt.subplots(2)
    
    
    def execute(self):
        print("> Please choose one of the equations below")
        for i, equation in enumerate(self.equations):
            if (i < 3): print("> {}. {}".format(i, equation.to_str()))
        print("> Enter your choice: ", end="")
        option = int(input())
        iteration_data = self.iteration_solver(option)
        bisection_data = self.bisection_solver(option)

        plt.show()
        self.show_table(iteration_data, bisection_data)

    def iteration_solver(self, option):
        iteration = EquationIterationMethod(self.equations[option])
        return self.solving(iteration, "SIMPLE ITERATION METHOD", option)
    
    def bisection_solver(self, option):
        bisection = BisectionMethod(self.equations[option])
        return self.solving(bisection, "BISECTION METHOD", option)

    def solving(self, method, name, option):
        self.axes[self.fig_num].set_title(name)
        self.axes[self.fig_num].grid(True)
        x = np.arange(-5 if option != 2 else 1, 5 if option != 2 else 10)
        y = self.equations[option].f(x)
        self.axes[self.fig_num].plot(x, y)

        print("> {} {} {}".format(self.DASH, name, self.DASH))
        ans, converge = 0, []
        try:
            ans, converge = method.execute()
            ans = round(ans, self.SCALE)
            self.axes[self.fig_num].plot([ans], [self.equations[option].f(ans)], "bo-")
        except:
            ans = "There is no solutions!"
        
        self.write_ans(ans, option)
        self.fig_num = self.fig_num + 1

        return converge

    def write_ans(self, ans, option):
        if (isinstance(ans, float)):
            print("> The solution of this equation is: {}".format(ans))
        else:
            print("> {}".format(ans))

    def show_table(self, bisection, iteration):
        if not bisection or not iteration: return

        sz = max(len(bisection), len(iteration))
        bisection, iteration = bisection + [bisection[-1]]* (sz - len(bisection)), iteration + [iteration[-1]] * (sz - len(iteration))
        for i in range(sz // 10 + 1):
            data = {"Chord": bisection[i * 10:min(i * 10 + 10, sz)],
                    "Iteration": iteration[i * 10:min(i * 10 + 10, sz)]}
            print(pd.DataFrame(data=data))
            if(i == sz // 10):
                print("> End.")
                break
            else:
                print("> Do you want to see more...? (Yes/No)")
                ans = input()
                if (ans == "No"): break
                else: 
                    self.reset()
                    self.execute()