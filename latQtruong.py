n,m,a = map(int,input().split())
# n: hang , m cot, a kich thuoc vien gach
x,y =0,0
# x chieu rong, y chieu dai 
if  n%a == 0:
    x = n // a
else: 
    x= n // a +1
if m %a == 0:
    y = m // a
else:
    y = m // a +1
print(x*y)