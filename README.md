# OlympiadVerify-Z3: Formal Reasoning for Competitive Mathematics

## Project Motivation
As a member of the **National Mathematics Commission** (for high school competitions) and a student at the **Faculty of Mathematics (MATF)**, University of Belgrade, I encountered a recurring challenge: ensuring the consistency and uniqueness of solutions for newly proposed competition problems. 

I built **OlympiadVerify-Z3** as a personal exploration into **Formal Methods** and **SMT Solvers**. My goal was twofold:
1. To automate the "sanity check" process for complex combinatorial and number theory problems.
2. To have fun exploring how abstract mathematical axioms can be translated into machine-verifiable logic.

## Implemented Features
The engine is built on top of the **Microsoft Z3 Theorem Prover** and features a modular Object-Oriented architecture:

### 1. Number Theory Module
- **General Fermat’s Little Theorem**: Verification for arbitrary primes.
- **Pell’s Equation Solver**: Bounded model checking for equations of the type $x^2 - Dy^2 = 1$.
- **Perfect Number Verifier**: Formalization of divisors and sum-properties.
- **State Competition Tasks**: Solving Diophantine equations involving prime constraints (e.g., $p^2 - 2q^2 = 1$).

### 2. Combinatorics & Graph Theory Module
- **Ramsey Theory**: Verifying $R(k, s)$ bounds through exhaustive state-space search.
- **Tournament Logic**: Proving the existence of a "king" in transitive tournaments (a frequent Serbian state competition topic).
- **Grid Coloring (Pigeonhole Principle)**: Proving the existence of monochromatic rectangles in colored grids.
- **Classic CS Problems**: Formal solutions to the **N-Queens problem**, **Latin Squares**, and the **Partition Problem (NP-Complete)**.

## Real-World Application
This tool can successfully verify several types of problems from the **Serbian State Mathematical Competitions (Category A/B)**, particularly those involving:
- Finite grid coloring and combinatorial geometry.
- Existence proofs in directed graphs (tournaments).
- Small-scale Diophantine analysis.
- See: State Competition 2018B, grade 2, problem 4; Regional 2021A, grade 1, problem1; SMO 2012; State 2015A, grade 4, problem 1
## Future Improvements & Generalization
This project is an evolving prototype. Potential areas for enhancement include:
- **DSL Integration**: Developing a Domain-Specific Language to input math problems in a LaTeX-like syntax rather than raw Python code.
- **Induction Engine**: Integrating Z3 with structural induction to prove properties for *all* $n$, not just within a bounded range.
- **Performance Optimization**: Implementing symmetry breaking in graph-related tasks to speed up Ramsey number verifications.
- **Proof Certificates**: Exporting Z3 results into formal proof assistants like **Lean** or **Coq** for absolute verification.

---
**Author:** Jovana  
**Field:** Mathematics and Computer Science @ MATF Belgrade  
**Interests:** Formal Methods, Automated Theorem Proving, Competitive Mathematics.
