def chuyencs(x, cso):
    #chuyen x sang coso moi va ktra thuan nghich
    digit = []
    while x> 0:
        digit.append(x % cso)
        x//=cso
    return digit == digit[::-1]

def dem(a,b,m):
    cnt = 0
    for x in range(a, b+1):
        ok = 1
        for cso in range(2, m+1):
            if not chuyencs(x,cso):
                ok = 0
                break
        if ok: cnt +=1
    return cnt

if __name__== '__main__':
    a,b,m = map(int,input().split())
    print(dem(a,b,m))

