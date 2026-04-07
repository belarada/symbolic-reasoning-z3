from z3 import *
from core.prover import OlympiadProver
from itertools import combinations

class CombinatoricsSuite(OlympiadProver):
    def __init__(self):
        super().__init__("Combinatorics Suite")

    def verify_graph_coloring(self, n, num_colors):
        """
        verify that a graph on n vertices can be colored with num_colors colors
        such taht adjacent vertices have different colors
        """
        self.name = f"Graph coloring n = {n}, colors = {num_colors}"
        self.solver.reset()

        adj = [[Bool(f"e_{i}_{j}") for j in range(n)] for i in range(n)]
        color = [Int(f"c_{i}") for i in range(n)]

        for i in range(n):
            self.add_condition(adj[i][i] == False)
            for j in range(i+1, n):
                self.add_condition(adj[i][j] == adj[j][i])

        for i in range(n):
            self.add_condition(color[i] >= 0, color[i] < num_colors)

        for i in range(n):
            for j in range(n):
                if i!= j:
                    self.add_condition(Implies(adj[i][j], color[i] != color[j]))
        
        if self.solver.check() == sat:
            print("Valid coloring exists")
            return self.solver.model()
        return None

    def verify_erdos_ko_rado(self, n, k, family_size):
        """
        Erdos-Ko-Rado: any family of k-seubsets of {1,...,n} that are pairwise intersecting
        has size <= C(n-1, k-1)
        """
        F = [[Bool(f"F_{i}_{j}") for j in range(n)] for i in range(family_size)]

        for i in range(family_size):
            self.add_condition(Sum([If(F[i][j], 1, 0) for j in range(n)]) == k)
        for i in range(family_size):
            for j in range(i+1, family_size):
                intersection = [And(F[i][t], F[j][t]) for t in range(n)]
                self.add_condition(Or(*intersection))
        if self.solver.check() == sat:
            print("Intersecting family exists")
            return self.solver.model()
        print("No such family")
        return None
        
    def check_ramsey(self, n, k_clique, s_independent):
        """ Ramsey R(k, s) > n verification using graph adjacency matrix """
        self.name = f"Ramsey R({k_clique}, {s_independent}) > {n}"
        self.solver.reset()
        adj = [[Bool(f"e_{i}_{j}") for j in range(n)] for i in range(n)]
        
        for i in range(n):
            self.add_condition(adj[i][i] == False)
            for j in range(i + 1, n):
                self.add_condition(adj[i][j] == adj[j][i])
        
        cliques = [And(*[adj[i][j] for i, j in combinations(c, 2)]) for c in combinations(range(n), k_clique)]
        indeps = [And(*[Not(adj[i][j]) for i, j in combinations(c, 2)]) for c in combinations(range(n), s_independent)]
        return self.prove(Or(*cliques, *indeps))

    def verify_grid_coloring_state(self, rows, cols, num_colors):
        """ Pigeonhole Principle: Monochromatic rectangles in colored grids """
        self.name = f"State Competition: Grid {rows}x{cols} Coloring"
        self.solver.reset()
        grid = [[Int(f"g_{i}_{j}") for j in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                self.add_condition(grid[i][j] >= 0, grid[i][j] < IntVal(num_colors))

        rects = []
        for r1, r2 in combinations(range(rows), 2):
            for c1, c2 in combinations(range(cols), 2):
                rects.append(And(grid[r1][c1] == grid[r1][c2], 
                                 grid[r1][c1] == grid[r2][c1], 
                                 grid[r1][c1] == grid[r2][c2]))
        return self.prove(Or(*rects))

    def verify_tournament_winner(self, n):
        """ Proving existence of a winner in transitive tournaments """
        self.name = f"Tournament Logic (n = {n})"
        self.solver.reset()
        win = [[Bool(f"w_{i}_{j}") for j in range(n)] for i in range(n)]
        
        for i in range(n):
            self.add_condition(win[i][i] == False)
            for j in range(i + 1, n):
                self.add_condition(win[i][j] == Not(win[j][i]))

        for i, j, k in combinations(range(n), 3):
            self.add_condition(Not(And(win[i][j], win[j][k], win[k][i])))
            self.add_condition(Not(And(win[k][j], win[j][i], win[i][k])))
            
        winners = [And([Or(win[i][j], i == j) for j in range(n)]) for i in range(n)]
        return self.prove(Or(*winners))

    def verify_latin_square(self, n=4):
        """ Constraint satisfaction for Latin Squares """
        self.name = f"Latin Square Completion (n={n})"
        self.solver.reset()
        cells = [[Int(f"s_{i}_{j}") for j in range(n)] for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                self.add_condition(cells[i][j] >= 1, cells[i][j] <= IntVal(n))
                
        for i in range(n):
            self.add_condition(Distinct(cells[i]))
        for j in range(n):
            self.add_condition(Distinct([cells[i][j] for i in range(n)]))
        
        if self.solver.check() == sat:
            print(f"Latin Square of order {n} found.")
            return self.solver.model()
        return None

    def verify_n_queens(self, n=8):
        """ Solving the classical N-Queens puzzle """
        self.name = f"{n}-Queens Problem"
        self.solver.reset()
        q = [Int(f"q_{i}") for i in range(n)]
        
        for i in range(n):
            self.add_condition(q[i] >= 0, q[i] < IntVal(n))
        self.add_condition(Distinct(q))
        
        for i in range(n):
            for j in range(i + 1, n):
                self.add_condition(q[i] - q[j] != IntVal(i - j))
                self.add_condition(q[i] - q[j] != IntVal(j - i))
        
        if self.solver.check() == sat:
            print(f"{n}-Queens solution exists")
            return self.solver.model()
        return None

    def verify_partition_problem(self, numbers):
        """ Partitioning a set into two subsets with equal sums """
        self.name = f"Partition Problem for {numbers}"
        self.solver.reset()
        n = len(numbers)
        belong_to_first = [Bool(f"b_{i}") for i in range(n)]
        
        sum1 = Sum([If(belong_to_first[i], IntVal(numbers[i]), IntVal(0)) for i in range(n)])
        sum2 = Sum([If(Not(belong_to_first[i]), IntVal(numbers[i]), IntVal(0)) for i in range(n)])
        
        self.solver.add(sum1 == sum2)
        if self.solver.check() == sat:
            print(f"Partition found for {numbers}")
            return self.solver.model()
        print(f"No partitions possible for {numbers}")
        return None
