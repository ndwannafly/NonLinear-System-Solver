from matplotlib import pyplot as plt
import numpy as np
from invokers.invoker import Invoker
from models.nonequation import NonlinearEquation
from solvers.equasolver import EquationSolver
from solvers.syssolver import SystemEquationSolver


if __name__ == '__main__':

    # x = np.arange(-5,5)
    # y = x ** 3 - 2 * x ** 2 + 1
    # plt.plot(x, y)
    # plt.show()

    np.seterr(all='raise')

    equations = [
        NonlinearEquation(lambda x: x ** 3 - 2 * x ** 2 + 1, lambda x: (2 * x ** 2 - 1) ** (1. / 3.), "x^3 - 2x^2 + 1 = y"),
        NonlinearEquation(lambda x: x - 1 - 0.5 * np.sin(x), lambda x: 1 + 0.5 * np.sin(x), "x - 1 - 0.5 * sin(x) = y"),
        NonlinearEquation(lambda x: np.log(x) + x ** 3 - x, lambda x: (x - np.log(x)) ** (1. / 3.), "ln(x) + x^3 - x = y"),
    ]

    equation_solver = EquationSolver(equations)
    system_equation_sovler = SystemEquationSolver() 

    invoker = Invoker(equation_solver, system_equation_sovler)
    invoker.invoke()

