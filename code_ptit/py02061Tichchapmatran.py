t = int(input())
while t:
    m, n = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    k = [list(map(int, input().split())) for _ in range(3)]
    tong = 0
    for row in range(m - 2):
        for col in range(n - 2):
            s = 0
            for h in range(3):
                for c in range(3):
                    s += k[h][c] * x[row + h][col + c]
            tong += s
    print(tong)
    t -= 1