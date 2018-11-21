import util

def solve(adj, order):
    cost = 0
    path = [0]
    visited = 1 # visit(int(''.join(['0']*order), 2), 0)
    idx = 0
    smallest = None
    while smallest != -1:
        smallest = -1
        for i in range(1, order):
            if i != idx\
                    and (smallest == -1 or
                         cost + adj[idx][i] + adj[i][0] < \
                         cost + adj[idx][smallest] + adj[smallest][0]) \
                    and not util.bit_check(visited, i):
                smallest = i

        if smallest != -1:
            cost += adj[idx][smallest]
            idx = smallest
            path.append(smallest)
            visited = util.bit_set(visited, smallest)

    cost += adj[idx][0] # loop back
    return path + [0], cost







