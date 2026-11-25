# Withdrawn candidate: 87/64 weight claim

**Date:** 2026-11-25  
**Status:** REJECTED after independent exhaustive audit

An earlier exploratory note reported an 11-vertex, 51-edge hypergraph with weight \(87/64\), allegedly without Property B. That claim was wrong.

Direct enumeration of all \(2^{11}=2048\) two-colorings finds **552 proper 2-colorings**. Therefore the candidate has Property B and is not a counterexample to any weighted non-2-colorability bound.

The exact edge-size profile and weight calculation were correct:
- 7 edges of size 4;
- 15 edges of size 5;
- 29 edges of size 6;
- total weight \(87/64\).

But the central property was false. The MILP search that purportedly surfaced the candidate had an indexing error in its mapping between vertex labels and coloring bits. Its output must not be used as evidence.

The script in \`experiments/hypergraph_weight_improvement.py\` is retained as an audit artifact. It reproduces the countercheck and prints the number of proper two-colorings.

**Conclusion:** withdraw the claimed improvement over Chan's \(11/8\) construction. No new mathematical result is claimed here. The corrected MILP encoding must be independently tested before any future candidate is reported.
