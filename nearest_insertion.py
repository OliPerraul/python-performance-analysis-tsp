import math
import util


def solve(adj, order):
    cost = 0
    path = [0]
    visited = 1 # visit(int(''.join(['0']*order), 2), 0)
    idx = 0
    smallest = None
    while smallest != -1:
        smallest = -1
        smallest_total = math.inf
        for i in range(1, order):
            if i != idx and not util.bit_check(visited, i):
                # We try to add the unvisited node which has smallest
                # dist to all other nodes in the path (aka the smallest total)
                total = 0
                for p in path:
                    total += adj[p][i]
                    if total >= smallest_total:
                        break
                if total < smallest_total:
                    smallest_total = total
                    smallest = i

        if smallest != -1:
            cost += adj[idx][smallest]
            idx = smallest
            path.append(smallest)
            visited = util.bit_set(visited, smallest)

    cost += adj[idx][0] # loop back
    return path + [0], cost







