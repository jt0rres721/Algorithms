class LinearPQ:
    def __init__(self):
        self.data = []  # list of (item, priority)

    def insert(self, item, priority):
        self.data.append([item, priority])

    def delete_min(self):
        if not self.data:
            raise IndexError("queue is empty can't delete min.")

        min_index = 0
        for i in range(1, len(self.data)):
            if self.data[i][1] < self.data[min_index][1]:
                min_index = i

        item, priority = self.data.pop(min_index)
        return item, priority

    def decrease_key(self, item, new_priority):
        for pair in self.data:
            if pair[0] == item:
                pair[1] = new_priority
                return

    def is_empty(self):
        return len(self.data) == 0

#Binary heap
class HeapPQ:
    def __init__(self):
        self.heap = []
        self.position = {}

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, item, priority):
        self.heap.append([item,priority])
        index = len(self.heap) - 1
        self.position[item] = index
        self._bubble_up(index)

    def delete_min(self):
        if self.is_empty():
            raise IndexError("queue is empty can't delete min.")

        min_item = self.heap[0]

        last = self.heap.pop()

        del self.position[min_item[0]]

        if self.heap:
            self.heap[0] = last
            self.position[last[0]] = 0
            self._bubble_down(0)

        return min_item[0], min_item[1]

    def decrease_key(self, item, new_priority):
        index = self.position[item]
        self.heap[index][1] = new_priority
        self._bubble_up(index)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][1] < self.heap[parent][1]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _bubble_down(self, index):
        size = len(self.heap)
        while True:
            left = 2*index + 1
            right = 2*index + 2
            smallest = index

            if left < size and self.heap[left][1] < self.heap[smallest][1]:
                smallest = left

            if right < size and self.heap[right][1] < self.heap[smallest][1]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.position[self.heap[i][0]] = j
        self.position[self.heap[j][0]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]





def find_shortest_path_with_heap(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the heap-based algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}

    dist[source] = 0

    pq = HeapPQ()
    for node in graph:
        pq.insert(node, dist[node])

    while not pq.is_empty():
        current, current_dist = pq.delete_min()

        if current_dist == float('inf'):
            break

        if current == target:
            break

        for edge, weight in graph[current].items():
            new_dist = dist[current] + weight
            if new_dist < dist[edge]:
                dist[edge] = new_dist
                prev[edge] = current
                pq.decrease_key(edge, new_dist)

    if dist[target] == float('inf'):
        return [], float('inf')

    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()
    return path, dist[target]


def find_shortest_path_with_linear_pq(
        graph: dict[int, dict[int, float]],
        source: int,
        target: int
) -> tuple[list[int], float]:
    """
    Find the shortest (least-cost) path from `source` to `target` in `graph`
    using the array-based (linear lookup) algorithm.

    Return:
        - the list of nodes (including `source` and `target`)
        - the cost of the path
    """
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}

    dist[source] = 0

    pq = LinearPQ()
    for node in graph:
        pq.insert(node, dist[node])

    while not pq.is_empty():
        current, current_dist = pq.delete_min()

        if current_dist == float('inf'):
            break

        if current == target:
            break

        for edge, weight in graph[current].items():
            new_dist = dist[current] + weight
            if new_dist < dist[edge]:
                dist[edge] = new_dist
                prev[edge] = current
                pq.decrease_key(edge, new_dist)

    if dist[target] == float('inf'):
        return [], float('inf')

    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()
    return path, dist[target]




