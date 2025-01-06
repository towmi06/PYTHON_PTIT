import itertools

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(itertools.permutations(range(1, n+1)) , reverse = True)
    print(len(a))
    for i in a:
        print(''.join(map(str,i)), end = ' ')
    print()
