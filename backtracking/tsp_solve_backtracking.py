import math
import random

from utils import Tour, SolutionStats, Timer, score_tour, Solver
from cuttree import CutTree


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

        stats.append(SolutionStats(
            tour=tour,
            score=cost,
            time=timer.time(),
            max_queue_size=1,
            n_nodes_expanded=n_nodes_expanded,
            n_nodes_pruned=n_nodes_pruned,
            n_leaves_covered=cut_tree.n_leaves_cut(),
            fraction_leaves_covered=cut_tree.fraction_leaves_covered()
        ))

    if not stats:
        return [SolutionStats(
            [],
            math.inf,
            timer.time(),
            1,
            n_nodes_expanded,
            n_nodes_pruned,
            cut_tree.n_leaves_cut(),
            cut_tree.fraction_leaves_covered()
        )]


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
    return []

def backtracking_bssf(edges: list[list[float]], timer: Timer) -> list[SolutionStats]:
    return []

