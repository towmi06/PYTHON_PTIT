from math import*
def isPrime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) +1):
        if n % i == 0: return False
    return True

def check (n):
    for i in range(0, len(n)):
        if isPrime(i) and not isPrime(int(n[i])):return False
        elif not isPrime(i) and isPrime(int(n[i])): return False
    return True

for i in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")