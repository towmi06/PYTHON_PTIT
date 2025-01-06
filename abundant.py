def sumD(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

def is_abundant(num):
    return sumD(num) > num

def find(n):
    a = []
    for i in range(1, n + 1):
        if is_abundant(i):
            a.append(i)
    return a

n = int(input())
a = find(n)
print(a)