import sys

def solve(adj, order):
    if order < 1:
        raise Exception("Minimum order of '1' is required.")
    if order == 1:
        return [0], 0
        
    cost = 0
    idx = 0
    path = [idx]
    visited = 1
    full = (1 << order)-1
    while visited != full:
        sidx = -1
        smallest = sys.maxsize
        for i in range(1, order):
            if (visited & (1 << i)) == 0 and adj[idx][i] < smallest:
                sidx = i
                smallest = adj[idx][sidx]

        cost += adj[idx][sidx]
        path.append(sidx)
        visited |= (1 << sidx)
        idx = sidx

    cost += adj[idx][0]
    path.append(0)
    return path, cost


CONTENT = ['Nearest Neighbor', 'red', solve]





