import random
import math
import datetime
import operator as op

import util
import brute_force
import nearest_neighbor
import nearest_insertion
import cheapest_insertion
import minimum_spanning_tree as mst


def write_randint_test_dataset(path, size):
    f = open(path, 'w')
    for i in range(size):
        f.write('DATASET' + str(i)+ '\n')
        for j in range(size):
            f.write(str(random.randint(0, size-1))+'\n')
    f.close()

def read_randint_test_dataset(path):
    f = open(path, "r")
    datasets = [[]]
    idx = 0
    while True:
        line = f.readline()
        if line:
            if 'DATASET' in line:
                datasets.append([])
                idx += 1
            else:
                val = int(line)
                datasets[idx].append(val)
        else:
            break
    return datasets

def test_randint(n):
    filename = 'randint{}'.format(datetime.datetime.now().timestamp())
    write_randint_test_dataset(filename, n)
    datasets = read_randint_test_dataset(filename)
    cumul = [0]*n
    for i in range(n):
        occurences = [0]*n
        for j in datasets[i]:
            occurences[j] += 1
        cumul = list(map(op.add, cumul, occurences))
    avgs = [float(x) / n for x in cumul]
    avg = sum(avgs)/n
    print('Upon generating ' + str(n) + ' datasets of size ' + str(n) + ', random.randint outputs each entry between 0 and ' + str(n-1) +', ' + str(avg) + ' times on average.')


def write_dataset(path, order, spread):
    #f = open("dataset_order{}_size{}_spread{}.txt".format(order, size, spread), "w")
    f = open(path, 'w')
    f.write('ORDER {}\n'.format(order))
    f.write('SPREAD {}\n'.format(spread))
    edges = 0
    adj = [[True]*order]*order # remember which connections we have done to prevent redundancy
    for i in range(order):
        # write point
        f.write('COORD')
        f.write(' ')
        f.write(str(random.randint(0, spread)))
        f.write(' ')
        f.write(str(random.randint(0, spread)))
        f.write('\n')
    f.close()

def distance(p1, p2):
    return math.sqrt( math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))


def read_dataset(path):
    f = open(path,"r")
    f2 = open(path+'.output',"w")
    lines = f.readlines()
    adj = None
    idx = -1
    cities = None
    order = 0
    for line in lines:
        vals = [int(s) for s in line.split() if s.isdigit()]
        if 'COORD' in line:
            idx += 1
            cities[idx] = vals
        elif 'ORDER' in line:
            order = vals[0]
            cities = [None]*vals[0]
            adj = [[None for i in range(vals[0])] for j in range(vals[0])]

    for i in range(len(cities)):
        p = cities[i]
        for j in range(len(cities)):
            if i != j:
                q = cities[j]
                dist = distance(p, q)
                adj[i][j] = distance(p, q)
            else:
                adj[i][j] = 0

    done = {}
    for i in range(order):
        for j in range(order):
            if i == j :
                continue
            if None == done.get(str(i)+','+str(j)):
                done[str(i)+','+str(j)] = True
                done[str(j)+','+str(i)] = True
                f2.write('e '+ str(i)+' '+ str(j)+' '+ str(adj[i][j]))
                f2.write('\n')

    f2.close()
    f.close()
    return adj, order

def validate(path, cost, adj):
    ccost = 0
    for i in range(len(path)-1):
        ccost += adj[path[i]][path[i+1]]
    ccost += adj[0][path[0]]  # first edge
    ccost += adj[util.end(path)][0] # last edge

    if not math.isclose(cost, ccost):
        raise Exception('Badly calculated path cost.')

def main():
    #test_randint(100)

    #while True:
        filename = 'dt' #'dataset{}'.format(datetime.datetime.now().timestamp())
        write_dataset(filename, 8, 30)
        adj, order = read_dataset(filename)

        print('Nearest neighbor')
        path, cost = nearest_neighbor.solve(adj, order)
        validate(path, cost, adj)
        print(path, cost)


        print('Nearest insertion')
        path, cost = nearest_insertion.solve(adj, order)
        validate(path,cost,adj)
        print(path,cost)

        print('Cheapest insertion')
        path, cost = cheapest_insertion.solve(adj, order)
        validate(path,cost,adj)
        print(path,cost)

        print('Minimum spanning tree')
        path, cost1 = mst.solve(adj, order, mst.DFS)
        validate(path,cost1,adj)
        print(path,cost1)

        print('Brute force')
        path, cost = brute_force.solve(adj, order)
        validate(path, cost, adj)
        print(path,cost)




main()



