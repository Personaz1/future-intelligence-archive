# Audit update: vertex-minimality search and edge-criticality

**Date:** 2026-11-25  
**Status:** Reproduced computational result; no portable infeasibility certificate yet

This note records a second, corrected run of the finite model described in `research/hypergraph-property-b-vertex-minimality.md`.

## Corrected independent run

I rebuilt the 10-vertex set-cover matrix using an explicit bit convention: vertex \(v>0\) is represented by bit \(v-1\), while vertex 0 is fixed to color 0. This removes global color-swap duplicates.

The rebuilt instance has:
- 10 vertices;
- 848 possible edges of sizes 4 through 10;
- 512 colorings up to global color swap;
- 26,025 nonzero coverage entries.

The strict weight condition \(w_2(H)<23/16\) is exactly the integer constraint
\[
\sum_e 2^{10-|e|}x_e\leq1471.
\]
SciPy 1.17.1 / HiGHS returned **infeasible** for this corrected model. Hypergraphs on fewer than 10 vertices embed by adding isolated vertices. This supports the claim that no example on at most 10 vertices can beat \(23/16\), under the model assumptions.

The result is a second local run, not an independently checkable proof certificate. HiGHS infeasibility still needs a portable certificate or a separate solver/checker before it can be promoted to a theorem.

## New exact observation: Chan's construction is edge-critical

The 11-vertex construction was reconstructed from the parity definition in Chan's paper. For each of its 24 edges, I removed that edge and exhaustively searched all \(2^{11}\) two-colorings. In every one of the 24 cases, at least one proper two-coloring appeared.

Therefore every edge is essential: the construction is **edge-critical non-2-colorable**. This is a finite, exact observation. It does not imply uniqueness or minimum weight.

The full checks also reproduce:
- 24 distinct edges: 20 of size 4 and 4 of size 5;
- zero proper 2-colorings;
- 92,874 proper 3-colorings;
- exact weight \(11/8\).

## Reproduction

The audited script is:
- `experiments/hypergraph_minimality_audited.py`

It reconstructs Chan's example, verifies edge-criticality by deletion tests, and runs the corrected 10-vertex MILP.

## Literature scope

Chan's paper already gives a parity proof of non-2-colorability and a finite Lean/Python verification of the construction. It does not claim the 10-vertex weighted lower bound or edge-criticality as a theorem. The 2023 Cherkashin survey treats the broader nonuniform weight problem and small cases.

Sources:
- Chan (2026), https://www.hbs.edu/ris/Publication%20Files/27-045_1_d8791a3c-cf18-40d7-8b2d-f880f713e92b.pdf
- Cherkashin (2023), https://doi.org/10.55630/mem.2023.52.71-75

## What remains open in this notebook

1. Produce a portable infeasibility certificate for the 10-vertex model.
2. Check the edge-criticality observation against the supplementary repository and broader literature before asserting novelty.
3. Search for a lower-weight construction using a corrected encoding.
