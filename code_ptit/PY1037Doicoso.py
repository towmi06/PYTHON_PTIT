f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if __name__ == '__main__':
    t = int(input())
    for i in range (t):
        n, coso = map(int,input().split())
        s = ''
        while n > 0:
            sodu = n %coso
            # vi so ngc tu duoi len
            s = f[sodu]+s
            n = n // coso
        print (s)

