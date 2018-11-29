import sys

def solve(adj, order):
    if order < 1:
        raise Exception("Minimum order of '1' is required.")
    if order == 1:
        return [0], 0

    # Search and perform an insertion
    # that will absolutely minimize the cost of the current circuit
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
        increase = sys.maxsize
        decrease = 0
        sinsert = -1
        sidx = -1
        for i in range(1, order):
            if (visited & (1 << i)) == 0:
                for j in range(0, len(path)-1):
                    p = path[j]
                    q = path[j + 1]
                    if adj[p][i] + adj[i][q] - adj[p][q] < increase - decrease:
                        increase = adj[p][i] + adj[i][q]
                        decrease = adj[p][q]
                        sidx = i
                        sinsert = j+1

        cost += increase
        cost -= decrease
        path.insert(sinsert, sidx)
        visited |= (1 << sidx)

    return path, cost



CONTENT = ['Cheapest Insertion', 'blue', solve]





