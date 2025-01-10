import random 

# duyet tu i+ 1 -> n-1 va luu vi tri tiep vao 1 bien tam
# sau khi duyet xong se doi cho 2 vi tri

def sinh(n):
    a =[]
    for _ in range(n):
        a.append(random.randint(0,100))
    return a

def sxchen(a):
    n = len(a)
    for i in range(1, n):
        tmp = a[i]
        j = i
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -=1
        
        a[j] = tmp
        print(f'Buoc {i} : {a}')

if __name__ == '__main__':
    a = sinh(10)
    print(a)
    sxchen(a)
    print(a)