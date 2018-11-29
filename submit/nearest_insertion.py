import sys

def solve(adj, order):
    if order < 1:
        raise Exception("Minimum order of '1' is required.")
    if order == 1:
        return [0], 0
		
    sidx = -1
    smallest = sys.maxsize
    for i in range(order):
        if i != 0 and adj[0][i] < smallest:
            smallest = adj[0][i]
            sidx = i

    path = [0, sidx, 0]
    cost = smallest*2
    visited = 1 | (1 << sidx)
    full = (1 << order) - 1
    while visited != full:
        # Search for the node, missing in the circuit,
        # whose distance from every other nodes in the circuit is minimal
        smallest = sys.maxsize
        sidx = -1
        for i in range(1, order):
            if (visited & (1 << i)) == 0: # every not visited
                total = 0
                for j in path[:len(path)-1]: #every visited
                     total += adj[i][j]
                if total < smallest:
                    smallest = total
                    sidx = i

        # Also, the node is inserted in such a way that minimizes the cost of the current circuit
        increase = sys.maxsize
        decrease = 0
        sinsert = -1
        for i in range(0, len(path)-1):
            p = path[i]
            q = path[i + 1]
            if adj[p][sidx] + adj[sidx][q] - adj[p][q] < increase - decrease:
                increase = adj[p][sidx] + adj[sidx][q]
                decrease = adj[p][q]
                sinsert = i+1

        cost += increase
        cost -= decrease
        path.insert(sinsert, sidx)
        visited |= (1 << sidx)

    return path, cost



CONTENT = ['Nearest Insertion', 'green', solve]





