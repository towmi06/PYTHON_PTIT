a, k, n = map(int,input().split())
ok = 0
if a + k >= n:
    print(-1)
else:
    for i in range(k - a% k, n+1-a, k):
        print(i, end= ' ')
#k - a % k giúp tìm min theo step = k mà bắt đầu từ a.
print(k - a%k)