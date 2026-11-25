"""Audited finite verification of Chan's Property-B example and 10-vertex bound.

Requires Python 3.10+, NumPy and SciPy (HiGHS MILP backend).
The MILP is a finite set-cover encoding. Its infeasibility result is
computer-assisted evidence, not a portable proof certificate.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix

def chan_edges():
    pairs = [(0, 1), (2, 3), (4, 5), (6, 7)]
    U = (8, 9, 10)
    edges = set()
    for pair in pairs:
        for subset in combinations(U, 2):
            edges.add(tuple(sorted(pair + subset)))
    for i, j, k in product((0, 1), repeat=3):
        transversal = (pairs[0][i], pairs[1][j], pairs[2][k])
        if (i + j + k) % 2 == 0:
            for d in pairs[3]:
                edges.add(tuple(sorted(transversal + (d,))))
        else:
            edges.add(tuple(sorted(transversal + pairs[3])))
    return sorted(edges)

def is_proper(edge, coloring):
    return len({coloring[v] for v in edge}) > 1

def verify_chan():
    edges = chan_edges()
    counts = dict(sorted(Counter(map(len, edges)).items()))
    weight = sum((Fraction(1, 2 ** len(e)) for e in edges), Fraction(0))
    proper_two = [c for c in product(range(2), repeat=11)
                  if all(is_proper(e, c) for e in edges)]
    proper_three = [c for c in product(range(3), repeat=11)
                    if all(is_proper(e, c) for e in edges)]
    critical_edges = 0
    for i in range(len(edges)):
        reduced = edges[:i] + edges[i + 1:]
        witness = next((c for c in product(range(2), repeat=11)
                        if all(is_proper(e, c) for e in reduced)), None)
        critical_edges += witness is not None
    assert len(edges) == 24 and counts == {4: 20, 5: 4}
    assert weight == Fraction(11, 8)
    assert not proper_two and proper_three
    assert critical_edges == 24
    return {
        "vertices": 11, "edges": 24, "edge_size_counts": counts,
        "proper_2_colorings": 0, "proper_3_colorings": len(proper_three),
        "weight": str(weight), "edge_critical_edges": critical_edges,
    }

def rule_out_10_vertices(time_limit=60):
    """Rule out weight <23/16 for non-2-colorable hypergraphs on <=10 vertices.

    Fix vertex 0 to color 0, leaving 2**9 colorings modulo color swap.
    For each possible edge, mark precisely the colorings it makes monochromatic.
    A chosen edge family is non-2-colorable iff every coloring is covered.
    """
    n = 10
    edges = [e for k in range(4, n + 1)
             for e in combinations(range(n), k)]
    assignments = np.arange(1 << (n - 1), dtype=np.int32)
    rows_all, cols_all = [], []
    for j, edge in enumerate(edges):
        mask = sum(1 << (v - 1) for v in edge if v > 0)
        values = assignments & mask
        mono = (values == 0) if 0 in edge else (
            (values == 0) | (values == mask)
        )
        rows = np.flatnonzero(mono)
        rows_all.extend(rows.tolist())
        cols_all.extend([j] * len(rows))
    cover = csr_matrix(
        (np.ones(len(rows_all)), (rows_all, cols_all)),
        shape=(1 << (n - 1), len(edges)),
    )
    scaled = np.array([2 ** (n - len(e)) for e in edges], dtype=np.int64)
    result = milp(
        c=np.zeros(len(edges)),
        integrality=np.ones(len(edges)),
        bounds=Bounds(0, 1),
        constraints=[
            LinearConstraint(cover, 1, np.inf),
            LinearConstraint(scaled.reshape(1, -1), -np.inf, 1471),
        ],
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    if result.status != 2:
        raise RuntimeError(f"Inconclusive MILP result: {result.message}")
    return {
        "vertices": n, "candidate_edges": len(edges),
        "colorings_up_to_swap": 1 << (n - 1),
        "coverage_nonzeros": cover.nnz,
        "scaled_weight_upper_bound": 1471,
        "solver_status": result.message,
    }

if __name__ == "__main__":
    print("Chan construction:", verify_chan())
    print("10-vertex MILP:", rule_out_10_vertices())
