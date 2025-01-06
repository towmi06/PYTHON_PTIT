class DanhSach:
    cnt = 0

    def __init__(self, ten, ma_team, ten_team, truong):
        DanhSach.cnt += 1
        self.ma = f'C{DanhSach.cnt:03d}'
        self.ten = ten
        self.ma_team = ma_team
        self.ten_team = ten_team
        self.truong = truong

    def __str__(self):
        return f'{self.ma} {self.ten} {self.ten_team} {self.truong}'


if __name__ == '__main__':
    t = int(input())
    teams = {}

    # Đọc thông tin các team
    for i in range(t):
        ten_team = input().strip()
        truong = input().strip()
        ma_team = f'Team{i + 1:02d}'
        teams[ma_team] = (ten_team, truong)


    n = int(input())
    ds = []

    for i in range(n):
        ten = input().strip()
        ma_team = input().strip()
        ten_team, truong = teams[ma_team]
        ds.append(DanhSach(ten, ma_team, ten_team, truong))

    ds.sort(key=lambda x: x.ten)

    for d in ds:
        print(d)
