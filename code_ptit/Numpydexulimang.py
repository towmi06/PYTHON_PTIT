import numpy as np
# chuyen tu 1 list orr tuple sang numpy, list:[], tuple(), dict{}
l = [1,9,4, 4, 6,7]
a = np.array(l)
print(a)
print(type(a))

k = [
    [16, 4, 7],
    [15, 8, 7],
    [17, 1, 26],
    [17, 7, 19]
]
b = np.array(k)
print(b)
print()
# ham b.ndim : kiem tra so chieu cua mang =2
#b.shape: xem smang co bao nhieu hang, bao nhieu cot
# b.size: kieu tra so phan tu cua mang
# np.array(l).reshape(so hang, so cot): tao array tu 1 list co san
# np.arange(begin, end, step): tao arr tu 1 day theo bdau, lt, bc nhay
# arange gan giong for i in range
# np.linspace(start, end, so luong): tao mang ma cac ptu deu nhau
# np.zeros((so hang, so cot)): mang toan 0
# np.ones((so hang, so cot )): mang toan 1
# access phan tu cua array : a[i,j] or a[i][j]
# access nhieu phan tu theo dong va cot : a[0:]: xuat dong indx 0
# a[:-1] xuat cot cuoi cung
# xuat phan tu thu 1 dong 1 den 2 nam trong cot 3: a[1:3,1]
# thay gia tri a[i,j] = 4
# thay nhieu gia tri o trong doan : vd: dong 1-2 cot 3: a[1:3, 1] = [10,33]
# kiem tra gia tri ton tai : 15 in a
# kiem tra vi tri cua no nam dau trong mang
for i in range (b.shape[0]):# hang
    for j in range (b.shape[1]):# cot bat dau tu chi so 1
        if b[i,j] == 16:
            print(i,j)

print()
print(b.ndim)
print(b.shape)
print(b.size)

x = np.array(l).reshape(2,3)
print(x)

z = np.linspace(1,10,6)
print(z)
