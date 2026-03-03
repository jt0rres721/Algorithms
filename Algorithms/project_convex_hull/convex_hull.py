from Algorithms.project_convex_hull.test_utils import cross
# from plotting import draw_line, draw_hull, circle_point


def compute_hull_dvcq(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    points = sorted(points, key=lambda p: (p[0], p[1]))

    return _compute_hull_recursive(points)

def _compute_hull_recursive(points):
    if len(points) <= 3:
        pts = sorted(points)

        if len(pts) <= 1:
            return pts

        if len(pts) == 2:
            return pts

        o, a, b = pts
        turn = cross(o, a, b)

        if turn > 0:
            return [o, a, b]
        elif turn < 0:
            return [o, b, a]
        else:
            return [o, b]

    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]

    left_hull = _compute_hull_recursive(left_points)
    right_hull = _compute_hull_recursive(right_points)

    return merge_hulls(left_hull, right_hull)


def merge_hulls(left, right):
    points = left + right
    points = sorted(points)

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def compute_hull_other(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    return []
