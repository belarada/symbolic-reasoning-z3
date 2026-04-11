from z3 import *
from core.prover import OlympiadProver

class NumberTheorySuite(OlympiadProver):
    def __init__(self):
        super().__init__("Number Theory Suite")

    def verify_pell_non_existence(self, D, bound=1000):
        """ Verify non existence of nontrivial solution to the equation x^2 - Dy^2 = 1 """
        self.name = f"Pell Equation x^2 - {D}y^2 = 1"
        x, y = Int('x'), Int('y')
        self.solver.reset()
        self.add_condition(x > 1, y > 1, x < IntVal(bound), y < IntVal(bound))
        
        claim = Not((x * x) - IntVal(D) * (y * y) == IntVal(1))
        return self.prove(claim)
    
    def verify_fermat_general(self, p_val):
        """ Fermat's Little theorem: n^p = n (mod p) """
        self.name = f"Fermat's Little Theorem (p={p_val})"
        n = Int('n')
        self.solver.reset()
        
        n_pow = n
        for _ in range(p_val - 1):
            n_pow = n_pow * n
            
        claim = ((n_pow - n) % IntVal(p_val) == 0)
        return self.prove(claim)

    def verify_prime_diophantine_state(self, primes_list):
        """ Problem from olympiad: p^2 - 2q^2 = 1 for primes p, q """
        self.name = "State Competition: Prime Diophantine p^2-2q^2 = 1"
        p, q = Int('p'), Int('q')
        self.solver.reset()
        p_is_prime = Or([p == IntVal(v) for v in primes_list])
        q_is_prime = Or([q == IntVal(v) for v in primes_list])
        self.add_condition(p_is_prime, q_is_prime)
        
        self.solver.add((p * p) - IntVal(2) * (q * q) == IntVal(1))
        
        if self.solver.check() == sat:
            print(f"Found a solution: {self.solver.model()}")
            return self.solver.model()
        return None

    def check_perfect_number(self, target=6):
        """ Verify if a number is perfect (sum of divisors equals the number) """
        self.name = f"Perfect Number Verification: {target}"
        self.solver.reset()
        divisors = [IntVal(i) for i in range(1, target) if target % i == 0]
        claim = (Sum(divisors) == IntVal(target))
        return self.prove(claim)

    def solve_linear_congruence_system(self, moduli_remainders):
        """ Solver for Chinese Remainder Theorem """
        self.name = "General CRT Solver"
        x = Int('x')
        self.solver.reset()
        for rem, mod in moduli_remainders:
            self.add_condition(x % IntVal(mod) == IntVal(rem))
        if self.solver.check() == sat:
            return self.solver.model()[x]
        return None
