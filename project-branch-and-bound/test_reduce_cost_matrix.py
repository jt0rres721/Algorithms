# See additional instructions for these tests in the instructions for the project
import math
import pytest
from tsp_solve import reduce_cost_matrix

INF =math.inf

def test_reduced_cost_matrix_1():
    matrix = [
        [INF, 3, 6, INF],
        [3, INF, 2, 3],
        [6, 2, INF, 5],
        [INF, 3, 5, INF],
    ]

    reduced, cost = reduce_cost_matrix(matrix)

    assert cost == 12, f"Expected cost 12, got {cost}"

    expected = [
        [INF, 0, 3, INF],
        [0, INF, 0, 0],
        [3, 0, INF, 2],
        [INF, 0, 2, INF],
    ]

    for r in range(4):
        for c in range(4):
            exp = expected[r][c]
            got = reduced[r][c]
            if exp == INF:
                assert got == INF, f"Cell [{r}][{c}]: expected INF, got {got}"
            else:
                assert got == pytest.approx(exp), (
                    f"Cell [{r}][{c}]: expected {exp}, got {got}"
                )


def test_reduced_cost_matrix_2():
    matrix = [
        [INF, 0, 4],
        [0, INF, 0],
        [3, 0, INF],
    ]

    reduced, cost = reduce_cost_matrix(matrix)

    assert cost == 0, f"Expected cost 0 for already-reduced matrix, got {cost}"

    expected = [
        [INF, 0, 4],
        [0, INF, 0],
        [3, 0, INF],
    ]

    for r in range(3):
        for c in range(3):
            exp = expected[r][c]
            got = reduced[r][c]
            if exp == INF:
                assert got == INF, f"Cell [{r}][{c}]: expected INF, got {got}"
            else:
                assert got == pytest.approx(exp), (
                    f"Cell [{r}][{c}]: expected {exp}, got {got}"
                )


# Add more tests as necessary...
