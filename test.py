import itertools

def bit_sets(p, n):
    result=[]
    for bits in itertools.combinations(range(n),p):
        s = ['0']*n
        for bit in bits:
            s[bit] = '1'
        result.append(int(''.join(s), 2))
    return result



for u in bit_sets(2, 4):
    print(bin(u))