import util

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
                    and not util.bit_check(visited, i):
                smallest = i

        if smallest != -1:
            cost += adj[idx][smallest]
            idx = smallest
            path.append(smallest)
            visited = util.bit_set(visited, smallest)

    cost += adj[idx][0] # loop back
    return [0] + path + [0], cost







