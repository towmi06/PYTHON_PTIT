from math import*

d ={5:10000, 7:15000, 2 : 20000, 29:50000, 45:70000}

if __name__ =='__main__':
    n = int(input())
    k = {}
    for _ in range(n):
        a = list(map(str,input().split()))
        seats = int(a[2])
        if a[3]=='IN':
            if a[-1] not in k:
                k[a[-1]] = 0
            k[a[-1]] += d[seats]
    for date, tien in k.items():
        print(f'{date}: {tien}')
    

