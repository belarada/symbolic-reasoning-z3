import sys
from examples.number_theory import NumberTheorySuite
from examples.combinatorics import CombinatoricsSuite

def run_full_verification():
    print("="*50)
    print("      OLYMPIAD VERIFY-Z3: FORMAL AUDIT SYSTEM    ")
    print("    Internal Audit Tool for National Math Commission")
    print("="*50)
    
    print("\n[SECTION 1: NUMBER THEORY]")
    nt_suite = NumberTheorySuite()
    
    nt_suite.verify_fermat_general(p_val=7)
    nt_suite.verify_pell_non_existence(D=3, bound=100)
    nt_suite.check_perfect_number(target=28)
    
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    nt_suite.verify_prime_diophantine_state(primes_list)
    
    print("\n" + "="*50)
    print("[SECTION 2: COMBINATORICS]")
    comb_suite = CombinatoricsSuite()
    
    comb_suite.check_ramsey(n=6, k_clique=3, s_independent=3)
    comb_suite.verify_grid_coloring_state(rows=3, cols=7, num_colors=2)
    comb_suite.verify_n_queens(n=8)
    comb_suite.verify_latin_square(n=4)
    comb_suite.verify_partition_problem([1, 5, 11, 5])
    comb_suite.verify_tournament_winner(n=5)
    
    print("\n" + "="*50)
    print("    FORMAL VERIFICATION COMPLETED SUCCESSFULLY")
    print("="*50)

if __name__ == "__main__":
    try:
        run_full_verification()
    except Exception as e:
        print(f"\n[ERROR] An error occurred during verification: {e}")
        sys.exit(1)
