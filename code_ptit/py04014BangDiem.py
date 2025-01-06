class Student:
    cnt = 0
    def __init__(self, ten, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10):
        Student.cnt += 1
        self.ma = f'HS{Student.cnt:02d}'
        self.ten = ten
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.m6 = m6
        self.m7 = m7
        self.m8 = m8
        self.m9 = m9
        self.m10 = m10

    def diem_tb(self):
        tv = (self.m1 + self.m2) * 2  
        total = (tv + self.m3 + self.m4 + self.m5 + self.m6
                 + self.m7 + self.m8 + self.m9 + self.m10)
        return total / 10/1.2

    def xep_loai(self):
        diem = self.diem_tb()
        if diem >= 9:
            return "XUAT SAC"
        elif 8 <= diem < 9:
            return "GIOI"
        elif 7 <= diem < 8:
            return "KHA"
        elif 5 <= diem < 7:
            return "TB"
        else:
            return "YEU"

    def __str__(self):
        return f'{self.ma} {self.ten} {self.diem_tb():.1f} {self.xep_loai()}'

if __name__ == "__main__":
    n = int(input())
    hs = []
    for _ in range(n):
        ten = input().strip()
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = map(float, input().split())
        hs.append(Student(ten, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10))

    # Sắp xếp theo điểm trung bình giảm dần
    hs.sort(key=lambda x: x.diem_tb(), reverse=True)

    print(*hs, sep="\n")
