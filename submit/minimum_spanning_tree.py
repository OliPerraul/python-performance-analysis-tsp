import sys
import heapq


class Node:
    def __lt__(self, other):
        return self.key < other.key

    def __init__(self):
        self.idx = -1
        self.parent = None
        self.key = sys.maxsize
        self.children = []

def last(ar):
    return ar[len(ar)-1]

def dfs_traversal(adj, root):
    path = []
    cost = 0
    stack = []
    stack.append(root)
    while len(stack) != 0:
        u = stack.pop()
        if len(path) != 0:
            cost += adj[last(path)][u.idx]
        path.append(u.idx)
        for v in u.children:
            stack.append(v)
    return path, cost

def calculate_hamiltonian_path(adj, root):
    path, cost = dfs_traversal(adj, root)
    cost += adj[last(path)][root.idx] # connect last with first
    path.append(root.idx)
    return path, cost

def calculate_mst(adj, order, root_idx):
    heap = []
    root = None
    for i in range(order):
        u = Node()
        u.idx = i
        if i == root_idx: # set root node as top
            root = u
            root.key = 0
        heapq.heappush(heap, u)

    while len(heap) != 0:
        u = heapq.heappop(heap)
        if u.parent != None:
            u.parent.children.append(u)
        for v in heap:
            if adj[u.idx][v.idx] < v.key:
                v.parent = u
                v.key = adj[u.idx][v.idx]
        heapq.heapify(heap)

    return root


def solve(adj, order):
    if order < 1:
        raise Exception("Minimum order of '1' is required.")
    if order == 1:
        return [0], 0
        
    root = calculate_mst(adj, order, 0)
    return calculate_hamiltonian_path(adj, root)



CONTENT = ['Minimum Spanning Tree', 'orange', solve]