from math import *
n, k = list(map(int, input().split()))

a = 10 ** (k - 1)
b = 10 ** k
cnt = 0

for i in range(a, b):
    if gcd(i, n) == 1:
        print(i, end = " ")
        cnt += 1
        if cnt % 10 == 0:
            print()
'''
a: số nhỏ nhất có 𝑘 chữ số (ví dụ, nếu 𝑘=3 thì a=100).
b: số đầu tiên lớn hơn số lớn nhất có 𝑘 chữ số (ví dụ, nếu 
𝑘=3, thì b=1000).
Với mỗi số i, kiểm tra nếu gcd(i, n) == 1:
Nếu đúng, i là số nguyên tố cùng nhau với 𝑛, in ra i.
Đếm số lượng số đã in (cnt) và sau mỗi 10 số thì in xuống dòng (cnt % 10 == 0).
'''