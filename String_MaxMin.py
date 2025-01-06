from math import*

if __name__ == '__main__':
    m,s = map(int,input().split())
    lon, be = [0]*m, [0]*m
    if s > 9 * m or ( s == 0 and m > 1):
        print('NOT FOUND')
    else:
        t = s
        for i in range(m):
            if s >= 9:
                lon[i] = 9
                s -= 9
            else:
                lon[i] = s
                s = 0
        #tinh so be, vi so be nhat phai bat dau bang 1 nen de danh 1 dv
        t-=1
        for i in range (m-1, 0,-1):
            if t >= 9:
                be[i]=9
                t -=9
            else:
                be[i] = t
                t = 0
        be[0] = t + 1
        print(*be, sep = '')
        print(*lon,sep ='')



