s = input()
a = {}
for i in range(len(s)//2):
    n = int(s[0]) * 10  + int(s[1])
    if n in a: a[n] +=1
    else: a[n] =1
    # loai bo 2 ki tu dau
    s = s[2::]
for i,j in a.items():
    print(i,j)