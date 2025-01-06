a,b,c = map(int, input().split())
x = a**2 + b**2
y = a**2 + c**2
z =c**2 + b**2
if(a >0) and b >0 and c > 0 and a+b>c and a+c >b and b+c >a:
    if(a == b == c): print('1')
    elif(a == b or a == c or b == c ): print('2')
    elif( x == c**2) or(y == b**2) or (z == a**2): print(3)
    else: print('4') 
else: print('INVALID')