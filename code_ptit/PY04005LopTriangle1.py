from math import sqrt

class Point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]
    def kc(self, other):
        return sqrt((self.x-other.x)*(self.x-other.x) + (self.y-other.y)*(self.y-other.y))

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def __str__(self):
        a = self.p1.kc(self.p2)
        b = self.p3.kc(self.p2)
        c = self.p1.kc(self.p3)
        return 'INVALID' if max(a, b, c) * 2 >= a + b + c else '{:.3f}'.format(a + b + c)

list, t, i = [], int(input()), 0
for __ in range(t):
    list += [float(i) for i in input().split()]
for __ in range(t):
    print(Triangle(Point(list[i:i+2]), Point(list[i+2:i+4]), Point(list[i+4:i+6])))
    i += 6
# Nhập hết các testcase của t lưu vào list sau r mới in 1 loạt