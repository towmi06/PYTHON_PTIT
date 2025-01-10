from math import*

def nto(n):
    if n< 2: return 0
    for i in range(2, isqrt(n)+1):
        if n% i == 0: return 0
    return 1

if __name__ == '__main__':
    n,m = map(int,input().split())
    a =[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if nto(a[i][j]):
                a[i][j]=1
            else: a[i][j] = 0
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=' ')
        print()

