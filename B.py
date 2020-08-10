from itertools import combinations


def solve(dots):
    acc = 0
    for (x1, y1), (x2, y2) in combinations(dots, 2):
        if x1 != x2 and y1 != y2:
            if (x1, y2) in dots and (x2, y1) in dots:
                acc += 1
    return acc // 2


T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    dots = set()
    for _ in range(k):
        x,y = [int(t) for t in input().strip().split()]
        dots.add((x, y))
    print(solve(dots))
