class sophuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __add__(self, other):
        return sophuc(self.thuc + other.thuc, self.ao + other.ao)

    def __mul__(self, other):
        thuc = self.thuc * other.thuc - self.ao * other.ao
        ao = self.thuc * other.ao + self.ao * other.thuc
        return sophuc(thuc, ao)

    def square(self):
        return self * self

    def __str__(self):
        if self.ao >= 0: return f"{self.thuc} + {self.ao}i"
        else: return f"{self.thuc} - {abs(self.ao)}i"

def tinh(a, b, c, d):
    A = sophuc(a, b)
    B = sophuc(c, d)
    sum_ab = A + B
    C = sum_ab * A
    D = sum_ab.square()
    return f"{C}, {D}"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        print(tinh(a, b, c, d))
