

def bit_set(bits,k):
    return bits|(1<<k)

def bit_check(bits,k):
    return bits&(1<<k)!=0

def end(ar):
    if len(ar) == 0:
        return None
    return ar[len(ar)-1]

def empty(ar):
    return len(ar) == 0

def is_minheap(arr):
    return all(arr[i] >= arr[(i-1)//2] for i in range(1, len(arr)))