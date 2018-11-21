import math
import util
import sys
import heapq



# for simplicity I have chosen to represent using a matrix
# However for further optimisation an adjency list would have allowed to use a heap

DFS = 0

class MST():
    class Node:
        def __init__(self):
            self.parent=-1
            self.weight=-1  # since parent
            self.children=[]

    def _dfs_visit(self,idx,visited,path,cost):
        if not util.empty(path):
            cost+=self.adj[util.end(path)][idx]
        path.append(idx)
        visited=util.bit_set(visited,idx)
        for child in self.nodes[idx].children:
            if not util.bit_check(visited,child):
                visited,cost = self._dfs_visit(child,visited,path,cost)
        return visited,cost

    def to_hamiltonian_path(self, traversal):
        path = []
        cost = 0
        if traversal == DFS:
            visited, cost = self._dfs_visit(self.root, 0, path, cost)
        else:
            raise Exception('Wrong traversal method.')

        cost += self.adj[util.end(path)][self.root]
        path += [self.root]
        return path,cost


    def _dequeue(self,keys,included):
        min_key = sys.maxsize
        idx = -1
        for i in range(self.order):
            if min_key > keys[i] and not util.bit_check(included, i):
                min_key = keys[i]
                idx = i
        return idx


    def __init__(self,adj,order,root):
        included = 0  # visit(int(''.join(['0']*order), 2), 0)
        self.root = root
        self.nodes = [None]*order
        self.adj = adj
        self.order = order
        keys = [None]*order

        for i in range(order):
            keys[i] = sys.maxsize
            self.nodes[i] = self.Node()

        keys[root] = 0
        self.nodes[root].parent = -1

        for i in range(order):
            v = self._dequeue(keys, included)
            if v == -1:
                continue
            included = util.bit_set(included, v)
            if self.nodes[v].parent != -1:
                self.nodes[self.nodes[v].parent].children.append(v)

            for j in range(order):
                if j == v:
                    continue
                # check if v 'j' is already in mst and if not then check if key needs an update or not
                if not util.bit_check(included, j) and adj[v][j] < keys[j]:
                    keys[j] = adj[v][j]
                    self.nodes[j].parent = v
                    self.nodes[j].weight = keys[j]

def solve(adj, order, traversal=DFS):
    mst = MST(adj, order, 0)
    return mst.to_hamiltonian_path(traversal)
