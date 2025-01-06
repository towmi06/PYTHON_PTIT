a,b, c, = map(int,input().split())
# a la so tien, b gia loai 1l, c gia loai 2l
if b<= c/2:
    print(a*b)
elif a%2 == 0:
    print(a//2*c)
else: print((a-1)//2*c +b)