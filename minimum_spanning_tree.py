import math
import util
import sys
import heapq


DFS = 0

class MST():
    class Node:
        def __lt__(self, other):
            return self.key < other.key

        def __eq__(self, other):
            return math.isclose(self.key, other.key)

        def __gt__(self, other):
            return self.key > other.key

        def __ge__(self, other):
            return self.key > other.key or math.isclose(self.key, other.key)

        def __le__(self, other):
            return self.key < other.key or math.isclose(self.key, other.key)

        def __init__(self):
            self.idx = -1
            self.parent = -1
            self.key = sys.maxsize
            self.children = []


    def _dfs_visit(self, idx, visited, path, cost):
        if not util.empty(path):
            cost += self.adj[util.end(path)][idx]
        path.append(idx)
        visited = util.bit_set(visited, idx)
        for child in self.nodes[idx].children:
            if not util.bit_check(visited, child):
                visited, cost = self._dfs_visit(child, visited, path, cost)
        return visited, cost

    def to_hamiltonian_path(self, traversal):
        path = []
        cost = 0
        if traversal == DFS:
            visited, cost = self._dfs_visit(self.root, 0, path, cost)
        else:
            raise Exception('Wrong traversal method.')

        cost += self.adj[util.end(path)][self.root]
        path += [self.root]
        return path, cost


    def __init__(self, adj, order, root):
        self.adj = adj
        self.order = order
        self.root = root
        heap = []
        self.nodes = [None]*order
        for i in range(order):
            self.nodes[i] = self.Node()
            self.nodes[i].idx = i
            if i == root: # set root node as top
                self.nodes[i].key = 0
            heapq.heappush(heap, self.nodes[i])

        while not util.empty(heap):
            u = heapq.heappop(heap)
            included = util.bit_set(included, u.idx)
            if u.parent != -1:
                self.nodes[u.parent].children.append(u.idx)
            for i in range(len(heap)):
                if adj[u.idx][heap[i].idx] < heap[i].key:
                    heap[i].parent = u.idx
                    heap[i].key = adj[u.idx][heap[i].idx]
                    heapq._siftdown(heap, 0, i) # value is decreased, sift down


def solve(adj, order, traversal=DFS):
    mst = MST(adj, order, 0)
    return mst.to_hamiltonian_path(traversal)
