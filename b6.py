import math

def strong(n):
    f = sum(math.factorial(int(digit)) for digit in str(n))
    return f == n

def find(n):
    strong_numbers = [i for i in range(1, n + 1) if strong(i)]
    return strong_numbers
if __name__ == '__main__':
    n = int(input())
    strong_numbers = find(n)
    print(*strong_numbers)