n,m = map(int,input().split())

if(n % 2 == 0):
    #số lương thanh dmino 1 cột * sô cột
    print(n//2*m)
else: print((n-1)//2*m+m//2)
# m //2 là số thanh domino của hàng cuối cùng 