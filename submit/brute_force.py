import math

def last(ar):
    if len(ar) == 0:
        return None

    return ar[len(ar)-1]

def next_permutation(v, n):
    i = n - 1 # longest non-increasing suffix
    while i > 0 and v[i-1] >= v[i]: # now i is the head of the suffix
        i -= 1

    if i <= 0:
        return None

    j = n-1
    while v[j] <= v[i-1]:
        j -= 1

    v[i-1], v[j] = v[j], v[i-1]
    j = n-1
    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1

    return v

def shortest_path(path1, cost1, path2, adj, order):
    cost2 = 0
    for i in range(len(path2)-1):
        cost2 += adj[path2[i]][path2[i+1]]
        if cost2 >= cost1:
            return path1, cost1

    cost2 += adj[0][path2[0]] # first edge
    cost2 += adj[last(path2)][0] # last edge
    if cost2 >= cost1:
        return path1, cost1

    return path2.copy(), cost2


def solve(adj, order):
    if order < 1:
        raise Exception("Minimum order of '1' is required.")
    if order == 1:
        return [0], 0

    path1, cost1 = shortest_path(None, math.inf, [i for i in range(1, order)], adj, order)
    path2 = path1.copy()
    path2 = next_permutation(path2, len(path2))
    while path2 != None:
        path1, cost1 = shortest_path(path1, cost1, path2, adj, order)
        path2 = next_permutation(path2, len(path2))

    path = [0]
    path.extend(path1)
    path.append(0)
    return path, cost1



CONTENT = ['Brute Force', 'pink', solve]