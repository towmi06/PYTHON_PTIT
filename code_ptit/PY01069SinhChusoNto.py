import itertools
n = int(input())
d ='2357'
res = []
# sinh tat ca cac so co tu 4 -> n 
for i in range(4, n+1):
    for j in itertools.product(d, repeat =i):
        k = ''.join(j)
        if '2'in k and '3' in k and '5'in k and '7' in k and int(k[-1]) %2 !=0:
            res.append(int(k))
    for i in sorted(res):
        print(i)