def nto(n):
    if n < 2: return 0
    for i in range (n):
        if n % i == 0:
            return 0
    return 1
if __name__ == '__main__':
    n = int(input())
    for i in range(1, (n//2)+1):
        if nto(i) and nto(n-i) :
            print(i, n-i)
            break
        else:
            print("Not found.")