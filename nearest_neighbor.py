import time


def solve(adj, order):
    cost = 0
    path = []
    visited = 1
    idx = 0
    smallest = 0
    while smallest != -1:
        smallest = -1
        for i in range(1, order):
            if i != idx \
                    and (smallest == -1 or adj[idx][i] < adj[idx][smallest])\
                    and not (visited & (1 << i)) != 0: # bit check
                smallest = i

        if smallest != -1:
            cost += adj[idx][smallest]
            idx = smallest
            path.append(smallest)
            visited |= (1 << smallest) # bit set

    cost += adj[idx][0] # loop back
    path = [0] + path + [0]

    return path, cost


CONTENT = ['Nearest Neighbor', 'red', solve]





