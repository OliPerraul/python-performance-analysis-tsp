
import random
import datetime
import operator as op
import os

import util


class Dataset:
    def __init__(self):
        self.adj = None
        self.order = -1


def write_randint_test(path,size):
    f = open(path, 'w')
    for i in range(size):
        f.write('DATASET' + str(i)+ '\n')
        for j in range(size):
            f.write(str(random.randint(0, size-1))+'\n')
    f.close()

def read_randint_test(path):
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
    write_randint_test(filename,n)
    datasets = read_randint_test(filename)
    cumul = [0]*n
    for i in range(n):
        occurences = [0]*n
        for j in datasets[i]:
            occurences[j] += 1
        cumul = list(map(op.add, cumul, occurences))
    avgs = [float(x) / n for x in cumul]
    avg = sum(avgs)/n
    print('Upon generating ' + str(n) + ' datasets of size ' + str(n) + ', random.randint outputs each entry between 0 and ' + str(n-1) +', ' + str(avg) + ' times on average.')


def read(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    order = -1
    adj = None
    for i in range(len(lines)):
        line = lines[i]
        vals = [float(s) for s in line.split() if util.isfloat(s)]
        if i == 0:
            order = int(vals[0])
            adj = [[None for i in range(order)] for j in range(order)]
        else:
            adj[int(vals[0])][int(vals[1])] = vals[2]
    return adj, order

def generate(order, spread, writepath=None):
    adj = [[None for i in range(order)] for j in range(order)]
    cities = [None]*order

    for i in range(order):
        cities[i] = (random.randint(0, spread), random.randint(0, spread))

    if writepath != None:
        f = open(writepath,'w')
        f.write(str(order))
        f.write('\n')

    for i in range(order):
        p = cities[i]
        for j in range(order):
            if i != j:
                q = cities[j]
                adj[i][j] = util.distance(p, q)
            else:
                adj[i][j] = 0

            if writepath != None:
                f.write(str(i))
                f.write(' ')
                f.write(str(j))
                f.write(' ')
                f.write(str(adj[i][j]))
                f.write('\n')

    if writepath != None:
        f.close()
    return adj
