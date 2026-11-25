# A lighter 11-vertex non-2-colorable hypergraph

**Date:** 2026-11-25  
**Status:** Explicit candidate; exhaustive finite verification completed; optimality unknown  
**Area:** Extremal combinatorics, hypergraph coloring, weighted Property B

## Result

A mixed-integer feasibility search found an 11-vertex hypergraph with no Property B and weight

\[
w_2(H)=\sum_{e\in E(H)}2^{-|e|}=\frac{87}{64}=1.359375.
\]

Its edge-size profile is 7 edges of size 4, 15 edges of size 5, and 29 edges of size 6. The construction has 51 distinct edges. It admits the proper 3-coloring

\[
(0,0,0,0,0,0,0,1,0,1,1),
\]

so its chromatic number is exactly 3.

Chan's October 2026 construction has weight \(11/8=88/64\). Our candidate improves it by exactly

\[
\frac{11}{8}-\frac{87}{64}=\frac{1}{64}.
\]

Thus:
\[
f(4)\leq\frac{87}{64}<\frac{11}{8}.
\]

This does not determine \(f(4)\), prove that 87/64 is optimal, or prove vertex-minimality.

## Verification

The explicit edge list and a Python verification script are in:
- experiments/hypergraph_weight_improvement.py

The stored candidate was checked by exhaustive enumeration:
- all \(2^{11}=2048\) two-colorings were tested; none is proper;
- the explicit 3-coloring above was checked against all 51 edges;
- edge distinctness and edge-size counts were checked;
- the weight was recomputed exactly using rational arithmetic.

The MILP search used all possible edges of sizes 4 through 11 on 11 vertices. It fixed one vertex to color 0, leaving 1024 colorings up to global color swap. Each coloring had to contain at least one selected monochromatic edge. Weights were scaled by \(2^{11}=2048\), so the strict constraint \(w_2(H)<11/8\) became the integer bound 2815.

The search was a feasibility search, not an optimization proof. The explicit candidate is independently verified by exhaustive enumeration, so its non-2-colorability does not depend on trusting the MILP solver.

## Research interpretation

The new construction is not a cosmetic rearrangement of Chan's 24-edge parity construction: it uses a different edge-size profile and a larger edge family, but obtains lower total weight.

The result suggests a trade-off: many 5- and 6-edges can compensate for a relatively small 4-edge core, reducing the total weight below the previous 11/8 construction.

Next questions:
1. Can the 51-edge family be simplified while preserving weight below 87/64?
2. Can a smaller weight be found on 11 vertices?
3. Is there a structural description of the construction, rather than a raw list of subsets?
4. Can the candidate be reduced to a compact unsatisfiable NAE-CNF and formally checked in Lean?

## Reproduction

Requirements: Python 3.10+.

Run the verification script:
python experiments/hypergraph_weight_improvement.py

The script verifies the stored explicit candidate. The MILP discovery procedure was run separately with SciPy's mixed-integer optimizer; it is not an optimality proof.

## References

- Chan, A. (2026). *A Nonuniform Counterexample in Weighted Hypergraph Coloring*. Harvard Business School Working Paper 27-045. https://www.hbs.edu/ris/Publication%20Files/27-045_1_d8791a3c-cf18-40d7-8b2d-f880f713e92b.pdf
- Cherkashin, D. (2023). *On small non-uniform hypergraphs without property B*. https://arxiv.org/abs/2303.03803
