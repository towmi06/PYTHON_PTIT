from datetime import datetime

class Phim:
    cnt = 0

    def __init__(self, ma_theloai, ten_theloai, ngay, ten, so_tap):
        Phim.cnt += 1
        self.ma = f'P{Phim.cnt:03d}'
        self.ma_theloai = ma_theloai
        self.ten_theloai = ten_theloai
        self.ngay = datetime.strptime(ngay.strip(), '%d/%m/%Y')
        self.ten = ten.strip()
        self.so_tap = so_tap

    def __str__(self):
        return f'{self.ma} {self.ten_theloai} {self.ngay.strftime("%d/%m/%Y")} {self.ten} {self.so_tap}'

if __name__ == '__main__':
    n, m = map(int, input().split())
    theloai_dict = {}
    for i in range(1, n + 1):
        ma_theloai = f'TL{i:03d}'
        ten_theloai = input().strip()
        theloai_dict[ma_theloai] = ten_theloai
    # Nhập danh sách phim
    phim_list = []
    for _ in range(m):
        ma_theloai = input().strip()
        ngay_khoi_chieu = input().strip()
        ten_phim = input().strip()
        so_tap = int(input().strip())

        # Lấy tên thể loại từ từ điển
        ten_theloai = theloai_dict[ma_theloai]
        phim_list.append(Phim(ma_theloai, ten_theloai, ngay_khoi_chieu, ten_phim, so_tap))

    phim_list.sort(key=lambda x: (x.ngay, x.ten.lower(), -x.so_tap))
    print(*phim_list, sep='\n')
