from z3 import *

class OlympiadProver:
    def __init__(self, problem_name="Math Problem"):
        self.solver = Solver()
        self.name = str(problem_name)

    def add_condition(self, *constraints):
        for c in constraints:
            self.solver.add(c)

    def prove(self, claim):
        print(f"\n--- Verifying: {self.name} ---")
        self.solver.push()
        self.solver.add(Not(claim))
        
        result = self.solver.check()
        if result == unsat:
            print(f"SUCCESS: Property '{self.name}' is formally proved.")
            self.solver.pop()
            return True
        else:
            print(f"Counter-example: Property '{self.name}' is false.")
            self.solver.pop()
            return False
