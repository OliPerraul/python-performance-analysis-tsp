import sys
import math


def find(fn, list):
    for item in list:
        if fn(item):
            return item
    return None

def last(ar):
    if len(ar) == 0:
        return None
    return ar[len(ar)-1]


def average(lst):
    return sum(lst) / len(lst)


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def distance(p1, p2):
    return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))
