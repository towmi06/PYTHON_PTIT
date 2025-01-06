import time
from math import gcd
from itertools import combinations_with_replacement


def lcm(x, y):
    return (x * y) // gcd(x, y)


if __name__ == '__main__':
    mod = 10 ** 9 + 7
    n = int(input())

    for _ in range(n):
        a, b = map(int, input().split())

        # Tính LCM của dãy [a, b]
        lccm = 1
        for i in range(a, b + 1):
            lccm = lcm(lccm, i)

        # Lấy các ước của LCM
        divisors = []
        for i in range(1, int(lccm ** 0.5) + 1):
            if lccm % i == 0:
                divisors.append(i)
                if i != lccm // i:
                    divisors.append(lccm // i)

        divisors.sort()

        # Sử dụng itertools để duyệt các cặp (x, y)
        cnt = 0
        for x, y in combinations_with_replacement(divisors, 2):
            if gcd(x, y) == 1:  # Kiểm tra gcd(x, y)
                if x == y:
                    cnt = (cnt + 1) % mod
                else:
                    cnt = (cnt + 2) % mod  # Cặp (x, y) và (y, x)

        print(cnt)