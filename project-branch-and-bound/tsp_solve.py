import math
import random

from tsp_core import Tour, SolutionStats, Timer, score_tour, Solver
from tsp_cuttree import CutTree

PARAMS_FOR_SMART_BRANCH_AND_BOUND_SMART_TEST = {
    "n": 30,
    "euclidean": True,
    "reduction": 0.2,
    "normal": False,
    "seed": 312,
    "timeout": 20,
}


def random_tour(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    stats = []
    n_nodes_expanded = 0
    n_nodes_pruned = 0
    cut_tree = CutTree(len(edges))

    while True:
        if timer.time_out():
            return stats

        tour = random.sample(list(range(len(edges))), len(edges))
        n_nodes_expanded += 1

        cost = score_tour(tour, edges)
        if math.isinf(cost):
            n_nodes_pruned += 1
            cut_tree.cut(tour)
            continue

        if stats and cost > stats[-1].score:
            n_nodes_pruned += 1
            cut_tree.cut(tour)
            continue

        stats.append(
            SolutionStats(
                tour=tour,
                score=cost,
                time=timer.time(),
                max_queue_size=1,
                n_nodes_expanded=n_nodes_expanded,
                n_nodes_pruned=n_nodes_pruned,
                n_leaves_covered=cut_tree.n_leaves_cut(),
                fraction_leaves_covered=cut_tree.fraction_leaves_covered(),
            )
        )

    if not stats:
        return [
            SolutionStats(
                [],
                math.inf,
                timer.time(),
                1,
                n_nodes_expanded,
                n_nodes_pruned,
                cut_tree.n_leaves_cut(),
                cut_tree.fraction_leaves_covered(),
            )
        ]


def greedy_tour(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    n = len(edges)
    solutions = []
    best_score = math.inf

    #loop to iterate through different paths
    for i in range(n):
        unvisited = set(range(n))
        tour = [i]
        unvisited.remove(i)
        while unvisited and not timer.time_out():   #stops after visiting all nodes or timing out
            current = tour[-1]
            next_node = min(unvisited, key=lambda j: edges[current][j])
            tour.append(next_node)
            unvisited.remove(next_node)
        score = score_tour(tour, edges)

        if not math.isinf(score):
            if best_score > score:
                solutions.append(SolutionStats(tour, score, timer.time(), 0, 0, 0, 0, 0))
                best_score = score

    return solutions


def backtracking(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    n = len(edges)
    solutions = []
    best_score = math.inf
    stack = [([0], set(range(1, n)))]

    while stack and not timer.time_out():
        path, unvisited = stack.pop()

        if len(path) == n:
            score = score_tour(path, edges)
            if best_score > score:
                solutions.append(SolutionStats(path, score, timer.time(), 0, 0, 0, 0, 0))
                best_score = score

        else:
            for node in unvisited:
                new_path = path + [node]
                new_unvisited = unvisited - {node}
                stack.append((new_path,new_unvisited))

    return solutions



def branch_and_bound(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    return []


def branch_and_bound_smart(
    edges: list[list[float]], timer: Timer
) -> list[SolutionStats]:
    return []

def reduce_cost_matrix(matrix: list[list[float]]) -> tuple[list[list[float]], float]:
    n = len(matrix)
    m_copy = [row[:] for row in matrix]
    total_cost = 0.0

    #Row reduction
    for r in range(n):
        row_min = min(m_copy[r])
        if row_min == math.inf:
            continue
        if row_min == 0:
            continue
        total_cost += row_min
        for c in range(n):
            if m_copy[r][c] != math.inf:
                m_copy[r][c] = m_copy[r][c] - row_min


    #Column reduction
    for c in range(n):
        col_min = min(m_copy[r][c] for r in range(n))
        if col_min == math.inf:
            continue
        if col_min == 0:
            continue
        total_cost += col_min

        for r in range(n):
            if m_copy[r][c] != math.inf:
                m_copy[r][c] = m_copy[r][c] - col_min


    return m_copy, total_cost
