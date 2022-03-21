from solvers.solver import Solver


class SystemEquationSolver(Solver):
    SCALE = 3
    
    def __init__(self, systems):
        self.systems = systems
    
    def execute(self):
        print("> Please choose one of the system of nonlinear equations below:")
        for index, system in enumerate(self.systems):
            print("> {}. System {}".format(index, index))
            system.write()
        
        print("> Enter your variant: ", end="")
        option = int(input())

        self.strategy.set_system(self.systems[option])

        ans = self.strategy.execute()
        print("The solution of this system of nonlinear equations is: ", end = "")
        for value in ans: print(round(value, self.SCALE), end = " ")
        print()
    
    def set_strategy(self, strategy):
        self.strategy = strategy