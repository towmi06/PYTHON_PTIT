from math import*

def check(n):
    if n == 0 or n == 1: return False
    for i in range (2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        a,b = map(int,input().split())
        c = gcd(a,b)
        s = 0
        while c > 0:
            s += c % 10
            c //= 10
        print(s)
        print('YES' if check(s) else 'NO')