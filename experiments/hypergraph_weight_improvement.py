"""Verified 11-vertex weighted Property-B counterexample; Python 3.10+."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

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
THREE_COLORING = (0,0,0,0,0,0,0,1,0,1,1)

def proper(edge, coloring):
    return len({coloring[v] for v in edge}) > 1

def verify():
    assert len(EDGES) == len(set(EDGES)) == 51
    assert all(tuple(sorted(e)) == e and 4 <= len(e) <= 6 for e in EDGES)
    proper_two = sum(
        all(proper(e, c) for e in EDGES)
        for c in product(range(2), repeat=N)
    )
    assert proper_two == 0
    assert all(proper(e, THREE_COLORING) for e in EDGES)
    counts = dict(sorted(Counter(map(len, EDGES)).items()))
    weight = sum((Fraction(1, 2**len(e)) for e in EDGES), Fraction(0))
    assert counts == {4: 7, 5: 15, 6: 29}
    assert weight == Fraction(87, 64) < Fraction(11, 8)
    return {
        "vertices": N, "edges": len(EDGES), "edge_size_counts": counts,
        "proper_two_colorings": proper_two,
        "proper_three_coloring": THREE_COLORING,
        "weight": str(weight),
        "improvement_over_Chan": str(Fraction(11, 8) - weight),
    }

if __name__ == "__main__":
    print(verify())
