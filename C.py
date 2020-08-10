from math import gcd,comb


def solve(pyramid, h):
    num = 0
    for i,layer in enumerate(pyramid):
        for j,aij in enumerate(layer):
            num += aij * comb(i, j) * 2**(h-i)
    denom = 2 ** h
    g = gcd(num, denom)
    return (num // g, denom // g)


T = int(input().strip())
for _ in range(T):
    h = int(input().strip())
    pyramid = [[int(x) for x in input().strip().split()] for _ in range(h)]
    print(*solve(pyramid, h))
