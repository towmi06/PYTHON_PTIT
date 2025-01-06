from math import *

def tang(n):
    for i in range(1,len(n)):
        if n[i] < n[i -1]:
            return 0
    return 1
def giam(n):
    for i in range(1,len(n)):
        if n[i] > n[i-1]:
            return 0
    return 1

if __name__ == '__main__':
    n = input()
    print('YES' if (tang(n) or giam(n)) else 'NO')