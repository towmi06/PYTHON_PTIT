p = 'ABCDEFGHIKLMNOPQRSTUVWXYZ_.'
k,s = map(str,input().split())
k = int(k)
s = s[::-1]
for i in s:
    t = p.find(i)
    print(p[(t+k)%28], end = '')


