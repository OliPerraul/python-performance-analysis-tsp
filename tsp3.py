import random
import math
import itertools


def next_permutation(v,n):
    i = n-1 # longest non-increasing suffix
    while i > 0 and v[i-1] >= v[i]:
        i -= 1

    if i <= 0:
        return None
    j = n-1
    while v[j] <= v[i-1]:
        j -= 1
    v[i-1],v[j] = v[j],v[i-1]

    j = n-1
    while i <j:
        v[i],v[j] = v[j],v[i]
        i += 1
        j -= 1
    return v




"""
(1,3) 1
1,2 2 2 3 4 
3
4
"""
def write_dataset(path, order, size, spread):
    assert(size <= order*(order-1)/2)
    #f = open("dataset_order{}_size{}_spread{}.txt".format(order, size, spread), "w")
    f = open(path, 'w')
    f.write('ORDER {}\n'.format(order))
    f.write('SIZE {}\n'.format(size))
    f.write('SPREAD {}\n'.format(spread))
    f.write('START {}\n'.format(random.randint(0, order-1)))
    edges = 0
    adj = [[True]*order]*order # remember which connections we have done to prevent redundancy
    for i in range(order):
        # write point
        f.write('COORD')
        f.write(' ')
        f.write(str(random.randrange(0, spread)))
        f.write(' ')
        f.write(str(random.randrange(0, spread)))
        f.write('\n')
    print('finished')
    f.close()


def distance(p1, p2):
    return math.sqrt( math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))


def read_dataset(path):
    f = open(path,"r")
    lines = f.readlines()
    adj = None
    idx = -1
    coords = None
    order = 0
    size = 0
    start = -1
    for line in lines:
        vals = [int(s) for s in line.split() if s.isdigit()]
        if 'COORD' in line:
            idx += 1
            coords[idx] = vals
        elif 'START' in line:
            start=vals[0]
        elif 'SIZE' in line:
            size = vals[0]
            coords=[None]*vals[0]
            adj=[[None]*vals[0]]*vals[0]
        elif 'ORDER' in line:
            order=vals[0]
            coords = [None]*vals[0]
            adj = [[None]*vals[0]]*vals[0]

    for i in range(len(coords)):
        p = coords[i]
        for j in range(len(coords)):
            if i != j:
                q = coords[j]
                adj[i][j] = distance(p, q)

    print(adj)
    f.close()
    return adj, order, size, start


def nearest_neighbor_heuristic(adj, order, size, start):
    while True:
        idx = random.randint(0,order-1)
        small = -1
        for i in range(len(adj[idx])):
            if small -1 or adj[idx][i] < adj[idx][small]:
                small = i





def brute_force_optimal(adj, order, size, start):
    pass











#
# def dp_find_optimal_tour(start, adj, order, size, memo):
#     pass
#
# # construct a bitmask for the endstate and use that to do a lookup in our memo table
# def dp_find_min_cost(start, adj, order, size, memo):
#     end_state = (1 << order) - 1
#     min_tour_cost = math.inf
#
# # The bit_sets function generates all bit sets
# # of size n with i bits set to 1. e.g
# # combinations (3, 4) = {0111, 1011, 1101, 1110}
# def dp_permutations(p, n):
#     result = []
#     for bits in itertools.combinations(range(n), p):
#         s = ['0']*n
#         for bit in bits:
#             s[bit] = '1'
#         result.append(int(''.join(s), 2))
#     return result
#
#
# # returns true if the ith bit in 'subset' is not set (0)
# def dp_not_in(i, subset):
#     return ((1 << i) & subset) == 0
#
#
# def dp_solve(start, adj, order, size, memo):
#     # let i be the number of nodes in the partial tour (incr num one at the time)
#     for i in range(3, order):
#         # generates all bitset of length order and i bit set to one
#         # These represent subsets of visited nodes
#         for subset in dp_permutations(i, order):
#             # enforce the node start to be part of the generated subset
#             # Otherwise the subset is not valid since it could not have started
#             # at our designated starting node
#             if dp_not_in(start, subset): continue
#             for j in range(order): # where j represents the idx of the nxt node
#                 if j == start or dp_not_in(j, subset): continue # enforce be part of current subset
#                 # the subset's state without the next node
#                 # this is so we can lookup in the memo table
#                 # to figure out what the best partial tour value is when the
#                 # next node is not part of our completed subset.
#                 # Being able to look back and reuse parts of other partially completed tours
#                 # is essential to the dp aspect of this problem
#                 state = subset ^ (1 << j)
#                 min_dist = math.inf
#
#                 # for each end node
#                 # while the node is fixed in the scope of the inner loop
#                 # we try all possible end nodes of the current subset and try to see which
#                 # end node best optim this partial tour
#                 # the end node cannot be any of the start node, the next node, or not part of the current subset
#                 for k in range(order):
#                     if k == start or k == j or dp_not_in(k, subset):
#                         continue
#                     new_dist = memo[k][state] + adj[k][j]
#                     if new_dist < min_dist:
#                         min_dist = new_dist
#                 memo[j][subset] = min_dist # store best partial tour in the memo table
#
#
# def dp_setup(start, adj, order, size, memo):
#     for i in range(order):
#         if i == start : continue
#         else: # mask with bits start and i set to one hence the double bit shift
#             # Cache the optimal value from start to each node i
#             # This is trivially the value stored in the adj matrix
#             memo[i][1 << start | 1 << i] = adj[start][i]
#
#
# def dynamic_programming_optimal(start, adj, order, size):
#     memo = [[None]*order]*math.pow(2, order)
#     dp_setup(start, adj, order, size, memo)
#     dp_solve(start,adj,order,size,memo) # find opt value for each partial tour with n nodes
#     dp_find_min_cost(start, adj, order, size, memo) # reuse the info, to find the minimum tour value
#



write_dataset('dataset.txt', 100,100,200)
adj, order, size = read_dataset('dataset.txt')






# Goodness of a heuristic must be measured


# Best is upper bound to the optimal

# If L0 is the optimal
# Then Lh, soit chacune des solution
# Then Lh >= L0

# soit Lh = 34 (length of the heuristic solution

# Lh/L0 < (1 + lgn)/2

 
# if n = 15
# <= 2.5


# If we have a metric with n = 128
# Then the length of the heuristic solution will be
# withon 4 times the length of the optimal solution
#Lh/L0 <= (1 + lgn)/2
# Lh/L0 <= 4
# Lh <= 4*L0





# Dynamic prog
# 1, 1, 2, 3, 5, 8
"""
IDEA
arr[n] = fib(n) 


T(n) = #calls * t <= 2n + 1 -> O(n)

    fib(n, memo)


def fib(n, memo):
    if memo[n] != null:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result


"""

"""
TSP with DP
The main idea will be to compute the optimal solution for all the subpaths of length N
while using information from the already known optimal partial tours of length N-1

Before starting, make sure to select a node 0 <= S < N to be disignated starting node for the tour. 

Next, compute and store the optimal value from S to each node X (!= s). This will solve TSP
problem for all paths of length n = 2

To compute the optimal solution for paths of length 3, we need to remember (store) two things
from each of the n = 2 cases :

1) The set of visited nodes in the subpath
2) The index of the last visited node in the path

Together these two things form our dunamic programming state. The are N posible nodes that
we could have visited last and 2^N possible substets of the visited nodes

Therefore the spacece needed to store the anser to each subproblem is bounded by O(N2^N)

"""


"""
Visited Nodes as a bit field
THe best way to represent the set of visited nodes is to use a single 32 bit integer. A 
32-bit int is compact quick and allow for easy caching


"""










