from math import *

prime = [True] * (10 ** 6 + 1)
prime_count = [0] * (10 ** 6 + 1)  # Mảng tích lũy đếm số lượng số nguyên tố


def sieves():
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(10 ** 6) + 1):
        if prime[i]:
            for j in range(i * i, 10 ** 6 + 1, i):
                prime[j] = False
    # Xây dựng mảng prime_count, trong đó prime_count[i] lưu số lượng số nguyên tố <= i
    for i in range(1, 10 ** 6 + 1):
        prime_count[i] = prime_count[i - 1] + prime[i]


# Hàm đếm số lượng số nguyên tố <= n
def count_primes(n):
    return prime_count[n]


if __name__ == '__main__':
    sieves()
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(count_primes(n))
