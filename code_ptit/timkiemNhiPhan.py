import random

def sinhTangdan(n):
    mang = []
    sodau = random.randint(-100,100)
    mang.append(sodau)

    for i in range (1,n):
        # san sinh so ngau nhien tang dan be nhat bang so do va cach xa nhat la 10 don vi
        tang = random.randint(0,10)
        somoi = mang[i-1] + tang
        mang.append(somoi)

    return mang

def timNhiPhan (mang, x):
    # chia doi mang va bien trai va bien phai
    trai = 0
    phai = len(mang)-1
    while trai <= phai:
        giua = (trai + phai)//2
        if mang[giua] == x:
            return giua
        elif x < mang[giua]:
            phai = giua - 1
        else:
            trai = giua + 1
    return -1

if __name__ == '__main__':
    mang = sinhTangdan(50)
    print(mang)
    x = int(input())
    vtri = timNhiPhan(mang,x)
    if vtri != x:
        print (f'Gia tri tai vi tri {vtri} tai do x bang {x}')
    else:
        print ('No found')