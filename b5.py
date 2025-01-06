from math import*

def strong(n):
    o = n
    f = 0
    while n > 0:
        r = n % 10
        f += factorial(r)
        n = n // 10
    return 1 if f == o else 0


if __name__ == '__main__':
    n = int(input())
    print('YES' if strong(n) else 'No')