"""Reproducible finite search for vertex-minimality of Chan's Property-B counterexample.

Requires Python 3.10+ and SciPy with scipy.optimize.milp (HiGHS backend).
The MILP is a weighted set-cover encoding of non-2-colourability.
"""
from itertools import combinations, product
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix, csr_matrix


def verify_11_vertex_construction():
    pairs = [(0, 1), (2, 3), (4, 5), (6, 7)]  # A, B, C, D
    U = (8, 9, 10)
    edges = set()

    for pair in pairs:
        for subset in combinations(U, 2):
            edges.add(tuple(sorted(pair + subset)))

    for i, j, k in product((0, 1), repeat=3):
        if (i + j + k) % 2 == 0:
            transversal = (pairs[0][i], pairs[1][j], pairs[2][k])
            for d in pairs[3]:
                edges.add(tuple(sorted(transversal + (d,))))

    for i, j, k in product((0, 1), repeat=3):
        if (i + j + k) % 2 == 1:
            transversal = (pairs[0][i], pairs[1][j], pairs[2][k])
            edges.add(tuple(sorted(transversal + pairs[3])))

    def proper(coloring):
        return all(len({coloring[v] for v in edge}) > 1 for edge in edges)

    two_colourings = sum(
        proper(coloring) for coloring in product(range(2), repeat=11)
    )
    three_colourings = sum(
        proper(coloring) for coloring in product(range(3), repeat=11)
    )
    counts = {k: sum(len(edge) == k for edge in edges) for k in (4, 5)}
    weight = sum(2.0 ** (-len(edge)) for edge in edges)
    explicit_three_coloring = (0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 2)

    assert len(edges) == 24 and counts == {4: 20, 5: 4}
    assert two_colourings == 0 and proper(explicit_three_coloring)
    assert three_colourings > 0 and abs(weight - 11 / 8) < 1e-12
    return {
        "vertices": 11,
        "edges": len(edges),
        "edge_counts": counts,
        "proper_2_colourings": two_colourings,
        "proper_3_colourings": three_colourings,
        "weight": weight,
        "explicit_3_colouring": explicit_three_coloring,
    }


def rule_out_at_most_10_vertices(time_limit=120):
    """Test if a non-2-colourable hypergraph on 10 vertices can weigh <23/16.

    Smaller hypergraphs embed by adding isolated vertices. Fix vertex 0 to colour
    0 to remove the global colour-swap duplicate. All possible edges of sizes 4..10
    are included. Multiplying weights by 2**10 makes every objective coefficient
    integral; strict weight <23/16 is equivalent to scaled weight <=1471.
    """
    n = 10
    colourings = list(product((0, 1), repeat=n - 1))
    edges = [
        edge
        for k in range(4, n + 1)
        for edge in combinations(range(n), k)
    ]
    cover = lil_matrix((len(colourings), len(edges)), dtype=np.float64)

    for j, edge in enumerate(edges):
        for i, tail in enumerate(colourings):
            values = [0 if v == 0 else tail[v - 1] for v in edge]
            if all(value == values[0] for value in values):
                cover[i, j] = 1

    scaled_weights = np.array(
        [2 ** (n - len(edge)) for edge in edges], dtype=np.int64
    )
    constraints = [
        LinearConstraint(csr_matrix(cover), 1, np.inf),
        LinearConstraint(scaled_weights.reshape(1, -1), -np.inf, 1471),
    ]
    result = milp(
        c=np.zeros(len(edges)),
        integrality=np.ones(len(edges)),
        bounds=Bounds(0, 1),
        constraints=constraints,
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    if result.status != 2:  # HiGHS status 2 = proven infeasible
        raise RuntimeError(
            f"No definitive infeasibility result: status={result.status}; "
            f"{result.message}"
        )
    return {
        "vertices": n,
        "candidate_edges": len(edges),
        "colourings_up_to_swap": len(colourings),
        "nonzero_cover_entries": int(cover.nnz),
        "solver_status": result.message,
        "strict_weight_bound": "23/16",
    }


if __name__ == "__main__":
    print("Known construction:", verify_11_vertex_construction())
    print("MILP lower-bound search:", rule_out_at_most_10_vertices())
    print(
        "Interpretation: within the stated model, HiGHS reports that no "
        "non-2-colourable hypergraph on <=10 vertices with all edges of "
        "size >=4 can have weight <23/16. This is computational evidence, "
        "not yet a portable formal infeasibility certificate."
    )
