"""Audit of a withdrawn 11-vertex hypergraph candidate.

The candidate was initially reported with weight 87/64 and claimed to
have no Property B. Independent exhaustive enumeration disproved that
claim: it has 552 proper 2-colorings. It is NOT a counterexample.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

N = 11
EDGES = [
(0,1,8,10),(0,4,5,10),(0,5,8,10),(0,6,8,10),(0,7,9,10),
(1,5,6,7),(4,7,8,9),
(0,1,3,4,10),(0,1,6,9,10),(0,2,6,7,10),(0,2,6,9,10),
(1,2,4,7,8),(1,2,4,8,9),(1,3,5,6,9),(1,3,6,7,8),
(2,3,6,7,8),(2,4,5,7,8),(2,4,6,8,9),(3,4,6,7,8),
(3,4,6,8,9),(3,5,6,7,8),(4,5,6,8,9),
(0,1,2,3,9,10),(0,1,2,4,6,10),(0,1,2,4,7,10),
(0,1,3,5,9,10),(0,1,3,6,7,10),(0,1,4,6,7,10),
(0,1,4,7,8,10),(0,1,4,7,9,10),(0,1,4,8,9,10),
(0,2,3,4,6,10),(0,2,3,4,7,10),(0,2,3,5,7,10),
(0,2,3,5,9,10),(0,2,3,6,9,10),(0,2,3,7,8,10),
(0,2,4,5,6,10),(0,3,4,6,7,10),(0,3,4,6,9,10),
(0,3,4,7,8,10),(0,4,5,6,7,10),
(1,2,3,5,7,8),(1,2,3,5,8,9),(1,2,4,5,6,9),
(1,2,5,6,8,9),(1,2,5,7,8,9),(1,3,5,7,8,9),
(2,3,4,5,8,9),(2,3,5,6,8,9),(2,3,5,7,8,9)
]

def is_proper(edge, coloring):
    return len({coloring[v] for v in edge}) > 1

def audit():
    proper = [
        coloring
        for coloring in product(range(2), repeat=N)
        if all(is_proper(edge, coloring) for edge in EDGES)
    ]
    counts = dict(sorted(Counter(map(len, EDGES)).items()))
    weight = sum(
        (Fraction(1, 2 ** len(edge)) for edge in EDGES), Fraction(0)
    )
    return {
        "vertices": N,
        "edges": len(EDGES),
        "edge_size_counts": counts,
        "weight": str(weight),
        "proper_two_colorings": len(proper),
        "property_B": bool(proper),
        "status": "WITHDRAWN: not a non-2-colorable hypergraph",
    }

if __name__ == "__main__":
    print(audit())
