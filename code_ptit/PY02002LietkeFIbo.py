f=[0]*93
def fibo():
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for i in range(3, 93):
        f[i]= f[i-1] + f[i-2]
'''
fibo = [0, 1, 1]

for i in range(3, 93):
    fibo.append(fibo[i - 1] + fibo[i - 2])
'''
if __name__ == '__main__':
    n = int(input())
    fibo()
    for _ in range (n):
        a,b = map(int,input().split())
        for i in range(a, b+1):
            print(f[i], end = ' ')
