from math import*

def nto(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    # Liệt kê tất cả các cặp số
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) == 1:  # Kiểm tra ước chung lớn nhất bằng 1
                print(a[i], a[j])


