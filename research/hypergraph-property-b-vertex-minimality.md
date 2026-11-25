# Computational note: vertex minimality of the 11-vertex weighted hypergraph example

**Date:** 2026-11-25  
**Status:** Exploratory computer-assisted result; independent certificate still needed  
**Area:** Extremal combinatorics, hypergraph coloring, integer programming

## Question

Alex Chan (working paper, 24 October 2026) gives a 3-chromatic hypergraph on 11 vertices with 20 edges of size 4 and 4 edges of size 5. Its weight under (w_2(H)=\sum_{e\in E(H)}2^{-|e|}\) is

\[
20\cdot 2^{-4}+4\cdot 2^{-5}=11/8=22/16<23/16.
\]

The cited theorem of Östergård gives (m(4)=23), so every 4-uniform hypergraph without Property B has weight at least (23/16). Chan's construction therefore disproves uniform attainment for (n=4).

**Question we tested:** Is 11 the minimum possible number of vertices for any hypergraph with all edges of size at least 4, no Property B, and weight strictly below (23/16)?

Source: Alex Chan, *A Nonuniform Counterexample in Weighted Hypergraph Coloring* (2026), especially Sections 1–3: https://www.hbs.edu/ris/Publication%20Files/27-045_1_d8791a3c-cf18-40d7-8b2d-f880f713e92b.pdf

## Exact finite encoding

A hypergraph has Property B exactly when its vertices admit a 2-coloring with no monochromatic edge. Thus a hypergraph has no Property B iff every 2-coloring is covered by at least one monochromatic edge.

For a fixed 10-vertex ground set, enumerate every possible edge of size 4 through 10. Introduce a binary variable (x_e\in\{0,1\}) for each candidate edge.

For every 2-coloring (c), impose:

\[
\sum_{e:\ e\text{ is monochromatic under }c}x_e\geq1.
\]

Global color swapping gives duplicate colorings, so fix vertex 0 to color 0. This leaves (2^9=512) colorings. There are 848 possible edges and 26,025 nonzero entries in the coverage matrix.

The weight condition is:

\[
\sum_e 2^{-|e|}x_e < 23/16.
\]

Multiplying by (2^{10}=1024) makes all coefficients integral. Since the scaled total is an integer, the strict inequality is equivalent to:

\[
\sum_e 2^{10-|e|}x_e\leq1471.
\]

We asked SciPy's mixed-integer optimizer (HiGHS backend) whether this system is feasible.

## Result

HiGHS returned **infeasible** for the 10-vertex model.

Any hypergraph on fewer than 10 vertices can be embedded into a 10-vertex ground set by adding isolated vertices. Therefore, subject to the correctness of the MILP model and solver result, no example on 10 or fewer vertices can meet the strict weight bound.

We separately reconstructed Chan's 11-vertex construction from the parity definition in the paper and checked it by direct enumeration:

- 11 vertices;
- 24 distinct edges: 20 four-edges and 4 five-edges;
- zero proper 2-colorings among all (2^{11}) colorings;
- at least one proper 3-coloring (the paper's explicit coloring);
- weight exactly (11/8).

**Interpretation:** the published 11-vertex construction is vertex-minimal for this threshold and edge-size restriction, if the MILP infeasibility result is independently confirmed.

## Important limitations

This is not yet a formal mathematical proof of the lower bound. HiGHS reports an infeasibility result, but this run does not export a portable proof certificate that a separate trusted checker can verify. The model and its encoding are finite and explicit; the solver's conclusion still needs independent reproduction or a checkable certificate.

The result does not determine the exact value of (f(4)), the minimum possible weight among all admissible nonuniform hypergraphs. It only addresses the minimum number of vertices for beating the (23/16) threshold.

It also does not prove that the construction is edge-minimal or unique.

## Reproduction

Run:

```bash
python experiments/hypergraph_minimality.py
```

Requirements: Python 3.10+, NumPy, SciPy with `scipy.optimize.milp` and the HiGHS backend.

The script:
1. reconstructs the 11-vertex construction;
2. exhaustively checks its 2- and 3-colorability;
3. builds the 10-vertex weighted set-cover MILP;
4. reports the solver status.

## Next verification steps

1. Re-run with a second independent MILP/SAT solver.
2. Seek a portable infeasibility certificate or derive a human-readable combinatorial lower bound.
3. Inspect whether the argument can be strengthened to characterize equality or near-extremal cases.
4. Search for a smaller-weight construction on 11 or more vertices; do not assume Chan's example is weight-optimal.

## References

- Chan, A. (2026). *A Nonuniform Counterexample in Weighted Hypergraph Coloring*. Harvard Business School Working Paper 27-045. https://www.hbs.edu/ris/Publication%20Files/27-045_1_d8791a3c-cf18-40d7-8b2d-f880f713e92b.pdf
- Östergård, P. R. J. (2014). *On the minimum size of 4-uniform hypergraphs without Property B*. Discrete Applied Mathematics 163, 199–204. https://doi.org/10.1016/j.dam.2011.11.035
