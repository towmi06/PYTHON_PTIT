class Diem:
    cnt = 0

    def __init__(self, ten, scores):
        Diem.cnt += 1
        self.ma = f'HS{Diem.cnt:02d}'
        self.ten = ten
        self.scores = scores[::]

    def dtb(self):
        dtb =sum(self.scores) / 10
        return dtb

    def hocluc(self):
        x = self.dtb()
        if x >= 9:
            return 'XUAT SAC'
        elif x >= 8:
            return 'GIOI'
        elif x >= 7:
            return 'KHA'
        elif x >= 5:
            return 'TB'
        else:
            return 'YEU'

    def __str__(self):
        return f'{self.ma} {self.ten} {self.dtb():.1f} {self.hocluc()}'


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        hs = Diem(input(),list(map(float, input().split())))
        a.append(hs)

    # Sắp xếp giảm dần theo điểm trung bình, nếu bằng thì theo mã tăng dần
    a.sort(key=lambda x: (-x.dtb(), x.ma))
    for x in a:
        print(x)
