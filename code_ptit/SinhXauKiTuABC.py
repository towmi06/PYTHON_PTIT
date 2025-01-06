def Sinh(xau,dodai,a,b,c):
#`a`, `b`, `c` lần lượt là số lượng ký tự A, B, C hiện có trong xâu
    if len(xau) == dodai:
        if a > 0 and b > 0 and c > 0 and a <= b <= c:
            print(xau)
        return
    if len(xau) < dodai:
        Sinh(xau +'A', dodai, a +1,b,c)
        Sinh(xau +'B', dodai, a,b +1,c)
        Sinh(xau +'C', dodai, a,b,c +1)

if __name__ == '__main__':
    n = int(input())
    # Vi la 3 ki tu ABC nen bat dau tu chi so 3
    for i in range (3, n+1):
        Sinh('',i, 0,0,0)