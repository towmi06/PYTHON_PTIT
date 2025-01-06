from math import*

def nto (n):
    if n < 2: return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0: return False
    return True
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        cnt, cntN = 0, 0
        for i in s:
            if nto(int(i)): cnt +=1
            else: cntN +=1
        print('YES' if cnt > cntN and nto(len(s)) else 'NO')
