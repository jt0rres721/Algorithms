import random
import sys
from time import time

GRAPH = dict[str, list[str]]
sys.setrecursionlimit(10000)


def prepost(graph: GRAPH) -> list[dict[str, list[int]]]:
    """
    Return a list of DFS trees.
    Each tree is a dict mapping each node label to a list of [pre, post] order numbers.
    The graph should be searched in order of the keys in the dictionary.
    """
    visited = set()
    pre = {}
    post = {}
    time = 1
    trees = []

    def explore(v: str, nodes: set[str]):
        nonlocal time

        visited.add(v)
        nodes.add(v)
        pre[v] = time
        time += 1

        for u in graph.get(v, []):
            if u not in visited:
                explore(u, nodes)
        post[v] = time
        time += 1

    for v in graph:
        if v not in visited:
            tree_nodes = set()
            explore(v, tree_nodes)
            trees.append({u: [pre[u], post[u]] for u in tree_nodes})


    return trees


def find_sccs(graph: GRAPH) -> list[set[str]]:
    """
    Return a list of the strongly connected components in the graph.
    The list should be returned in order of sink-to-source
    """
    #Start by reversing the graph.
    reverse_graph = {}
    for node, edges in graph.items():
        for edge in edges:
            reverse_graph.setdefault(edge, []).append(node)

    trees = prepost(reverse_graph)

    post_order = {}
    for tree in trees:
        for node, (_, post) in tree.items():
            post_order[node] = post

    order = sorted(post_order, key=lambda v:post_order[v], reverse = True)

    visited = set()
    sccs = []

    def explore(v: str, comp: set[str]):
        visited.add(v)
        comp.add(v)
        for u in graph.get(v, []):
            if u not in visited:
                explore(u, comp)

    for v in order:
        if v not in visited:
            comp = set()
            explore(v, comp)
            sccs.append(comp)

    return sccs


def classify_edges(graph: GRAPH, trees: list[dict[str, list[int]]]) -> dict[str, set[tuple[str, str]]]:
    """
    Return a dictionary containing sets of each class of edges
    """
    classification = {
        'tree/forward': set(),
        'back': set(),
        'cross': set()
    }



    return classification


