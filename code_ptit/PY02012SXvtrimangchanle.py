# vi tri cac so chan le trong chuoi ban dau k thay doi 

n = int(input())
a, b, c, d = [], [], [], [0] * n
while True :
    x = [int(x) for x in input().split()]
    a += x
    if len(a) == n : break
for i in range(n) :
    if a[i] % 2 == 1 :
        b.append(a[i])
        d[i] = 1
    else : c.append(a[i])
b = sorted(b)
c = sorted(c,reverse = 1)
for i in range(n) :
    if d[i] == 1 :
        print(b[-1], end = " ")
        b.pop()
    else :
        print(c[-1], end = " ")
        c.pop()