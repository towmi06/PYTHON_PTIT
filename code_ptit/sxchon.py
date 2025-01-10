import random 
# sx chon
# i : 0 -> n-2 = range(0, n-1)
# j : i+1 -> n-1 = range(i+1, n)
# i se tim trong mang j gtri nho nhat
# neu tim thay thi doi cho 2 vi tri
def sinh(n):
    a = []
    for i in range(n):
        a.append(random.randint(1,100))
    return a

def sx(a):
    n = len(a)
    for i in range(n-1):
        ok = 0
        for j in range(i+1, n):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]
                ok = 1
        print(f'Buoc {i+1} - {a}')
        if ok == 0: break

if __name__ == '__main__':
    a = sinh(10)
    print(a)
    sx(a)
    print(a)
