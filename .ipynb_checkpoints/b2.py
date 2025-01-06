a, b = map(int,input().split())
if a == 0 or b == 0:
    print(0)
if b > 0 and a > 0:
    print (-b/a)
elif b < 0 or a < 0:
    print(b/a)
    # toan tu 3 ngoi 
    x = -b/a if a != 0 else "PT vo " + ("so"  if  b == 0 else '') + 'nghiem'