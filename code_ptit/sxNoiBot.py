import random
#Bubble Sort: sx noi bot
# san sinh so ngau nhien
# i : 0 -> n-2 = range(0, n-1)
# j : n-2 - > i = range(n-2, i-1, -1), j chay nguoc lai 
#  neu a[j] > a[j+1] thi doi 2 vi tri cho nhau
def sinh(n):
    a = []
    for i in range(n):
        a.append(random.randint(1,100))
    return a

# mang a chua duoc sap xep
def sxep(a):
    n = len(a)
    for i in range(n):
        tiep = 0
        for j in range(n-2, i-1, -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                tiep = 1
        print(f'Buoc {i+1} - {a}')

        if tiep == 0: break 

if __name__ == '__main__':
    #a =[3,5,98, 1 , 5 ,6,8,10]
    a = sinh(10)
    print(a)
    sxep(a)
    #mang sau khi sxep
    print(a)