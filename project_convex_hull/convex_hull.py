from project_convex_hull.test_utils import cross
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
    if not left:
        return right
    if not right:
        return left

    nL = len(left)
    nR = len(right)

    i = max(range(nL), key=lambda k: left[k][0])

    j = min(range(nR), key=lambda k: right[k][0])

    done = False
    while not done:
        done = True

        while cross(right[j], left[i], left[(i - 1) % nL]) >= 0:
            i = (i - 1) % nL

        while cross(left[i], right[j], right[(j + 1) % nR]) <= 0:
            j = (j + 1) % nR
            done = False

    upper_i = i
    upper_j = j

    i = max(range(nL), key=lambda k: left[k][0])
    j = min(range(nR), key=lambda k: right[k][0])

    done = False
    while not done:
        done = True

        while cross(right[j], left[i], left[(i + 1) % nL]) <= 0:
            i = (i + 1) % nL

        while cross(left[i], right[j], right[(j - 1) % nR]) >= 0:
            j = (j - 1) % nR
            done = False

    lower_i = i
    lower_j = j

    hull = []

    idx = upper_i
    hull.append(left[idx])
    while idx != lower_i:
        idx = (idx - 1) % nL
        hull.append(left[idx])

    idx = lower_j
    hull.append(right[idx])
    while idx != upper_j:
        idx = (idx - 1) % nR
        hull.append(right[idx])

    if len(hull) < 3:
        return hull

    total = 0
    for i in range(len(hull)):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % len(hull)]
        total += (x2 - x1) * (y2 + y1)

    if total > 0:
        hull = hull[::-1]

    return hull


def compute_hull_other(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull
       using the Monotone Chain algorithm."""

    if len(points) <= 1:
        return points

    # Sort points lexicographically
    points = sorted(points)

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Remove duplicate endpoints and combine
    hull = lower[:-1] + upper[:-1]

    return hull
