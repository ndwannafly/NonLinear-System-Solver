from solvers.solver import Solver


class Invoker:
    DASH = '-' * 10
    def __init__(self, equation_solver: Solver, system_equation_solver: Solver):
        self.equation_solver = equation_solver
        self.system_equation_solver = system_equation_solver

    def invoke(self):
        print("> {} Welcome to nonlinear world! {}".format(self.DASH, self.DASH))
        print("> Which type of problem do you want to solve?")
        print("> 1. Solve a nonlinear equation.")
        print("> 2. Solve a system of nonlinear equations")
        print("> Enter your option (1 or 2): ", end = "")
        option = int(input())
        if(option == 1):
            self.equation_solver.execute()
        else:
            self.system_equation_solver.execute()