for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l, r = max(a), min(a)
    cnt =0
    for i in range(l,r-1,-1):
        if i not in a: cnt +=1
    print(cnt)

