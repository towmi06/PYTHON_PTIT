n =int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
for i in a:
    if ans == i : ans += 1
print (ans)