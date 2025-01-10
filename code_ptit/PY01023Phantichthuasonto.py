from math import*

def thuasnt(n):
    f = {}
    cnt = 0
    # ktra snto tu 2 -> sqrt(n)
    for i in range (2, isqrt(n)+1):
        if n% i ==0: 
            cnt =0
            while n% i == 0:
                n //=i
                cnt += 1
                f[i]= cnt
    # neu n > 1 thi la thuasnt
    if  n > 1: f[n]=1
    return f

if __name__ =='__main__':
    for _ in range (int(input())):
        n = int(input())
        ans = thuasnt(n)
        
        res ='1'
        for i, j in ans.items():
            res += f' * {i}^{j}'
        print(res)
            
