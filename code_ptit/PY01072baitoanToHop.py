from itertools import*

n, k = map(int, input().split())
a = list(map(int, input().split()))

u = sorted(set(a))

for i in combinations(u, k):
    print(" ".join(map(str, i)))
