t = int(input())
a = []
for _ in range(t):
    ma = input()
    ten = input()
    ht = input()
    a.append((ma, ten, ht))

b = sorted(a, key=lambda x: x[0])

for x in b:
    print(' '.join(x))
