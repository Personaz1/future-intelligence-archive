# A lighter 11-vertex non-2-colorable hypergraph

**Date:** 2026-11-25  
**Status:** Explicit candidate; exhaustive finite verification completed; optimality unknown  
**Area:** Extremal combinatorics, hypergraph coloring, weighted Property B

## Result

An exploratory mixed-integer search surfaced an 11-vertex hypergraph with no Property B and weight

\[
w_2(H)=\sum_{e\in E(H)}2^{-|e|}=\frac{87}{64}=1.359375.
\]

Its edge-size profile is 7 edges of size 4, 15 edges of size 5, and 29 edges of size 6. The construction has 51 distinct edges. It admits the proper 3-coloring

\[
(0,0,0,0,0,0,0,1,0,1,1),
\]

so its chromatic number is exactly 3.

Chan's October 2026 construction has weight \(11/8=88/64\). This candidate improves it by exactly

\[
\frac{11}{8}-\frac{87}{64}=\frac{1}{64}.
\]

Thus:
\[
f(4)\leq\frac{87}{64}<\frac{11}{8}.
\]

This does not determine \(f(4)\), prove that 87/64 is optimal, or prove vertex-minimality.

## Verification and audit

The explicit edge list and a Python verification script are in:
- experiments/hypergraph_weight_improvement.py

The stored candidate was checked by direct exhaustive enumeration:
- all \(2^{11}=2048\) two-colorings were tested; none is proper;
- the explicit 3-coloring above was checked against all 51 edges;
- edge distinctness and edge-size counts were checked;
- the weight was recomputed exactly using rational arithmetic.

**Important audit correction:** the first MILP encoding used to surface this candidate contained an off-by-one error in mapping vertex labels to coloring bits. Therefore its solver output is not valid evidence for the general search claim, and no claim is made that the MILP correctly searched the full coloring space. The candidate itself remains valid because its full 2-coloring space was checked independently and exhaustively. The MILP search must be rerun with corrected bit indexing before its results are cited.

## Research interpretation

The construction is not a cosmetic rearrangement of Chan's 24-edge parity construction: it uses a different edge-size profile and a larger edge family, but obtains lower total weight.

The result suggests a trade-off: many 5- and 6-edges can compensate for a relatively small 4-edge core, reducing the total weight below the previous 11/8 construction.

Next questions:
1. Correct and rerun the full MILP search.
2. Can the 51-edge family be simplified while preserving weight below 87/64?
3. Can a smaller weight be found on 11 vertices?
4. Is there a structural description of the construction, rather than a raw list of subsets?
5. Can the candidate be reduced to a compact unsatisfiable NAE-CNF and formally checked in Lean?

## Reproduction

Requirements: Python 3.10+.

Run the verification script:
python experiments/hypergraph_weight_improvement.py

The script verifies the stored explicit candidate. It does not reproduce the MILP discovery or prove optimality.

## References

- Chan, A. (2026). *A Nonuniform Counterexample in Weighted Hypergraph Coloring*. Harvard Business School Working Paper 27-045. https://www.hbs.edu/ris/Publication%20Files/27-045_1_d8791a3c-cf18-40d7-8b2d-f880f713e92b.pdf
- Cherkashin, D. (2023). *On small non-uniform hypergraphs without property B*. https://arxiv.org/abs/2303.03803
