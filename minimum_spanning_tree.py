import math
import sys
import heapq

class Node:
    def __lt__(self, other):
        return self.key < other.key

    def __init__(self):
        self.idx = -1
        self.parent = -1
        self.key = sys.maxsize
        self.children = []

def last(ar):
    if len(ar) == 0:
        return None
    return ar[len(ar)-1]

def dfs_visit(adj, order, idx, nodes, path, cost, visited):
    if len(path) != 0:
        cost += adj[last(path)][idx]
    path.append(idx)
    visited |= (1 << idx)
    for child in nodes[idx].children:
        if not (visited & (1 << child)) != 0:
            visited, cost = dfs_visit(adj, order, child, nodes, path, cost, visited)
    return visited, cost

def calculate_hamiltonian_path(adj, order, root, nodes):
    path = []
    visited, cost = dfs_visit(adj, order, root, nodes, path, 0, 0)
    cost += adj[last(path)][root]
    path += [root]
    return path, cost

def calculate_mst(adj, order, root):
    heap = []
    nodes = [None]*order
    for i in range(order):
        nodes[i] = Node()
        nodes[i].idx = i
        if i == root: # set root node as top
            nodes[i].key = 0
        heapq.heappush(heap, nodes[i])
    included = 0
    while len(heap) != 0:
        u = heapq.heappop(heap)
        included |= (1 << u.idx) #bitset
        if u.parent != -1:
            nodes[u.parent].children.append(u.idx)
        for i in range(len(heap)):
            if adj[u.idx][heap[i].idx] < heap[i].key:
                heap[i].parent = u.idx
                heap[i].key = adj[u.idx][heap[i].idx]
                heapq._siftdown(heap, 0, i) # value at i is decreased, sift down

    return nodes


def solve(adj, order):
    root = 0
    nodes = calculate_mst(adj, order, root)
    return calculate_hamiltonian_path(adj, order, root, nodes)



CONTENT = ['Minimum Spanning Tree', 'yellow', solve]