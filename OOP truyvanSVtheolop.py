class SinhVien:
    def __init__(self, ma, ten, lop, email):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email

    def __str__(self):
        return f'{self.ma} {self.ten.title()} {self.lop} {self.email}'


if __name__ == '__main__':
    # Đọc danh sách sinh viên
    n = int(input())
    a = []
    for _ in range(n):
        sv = SinhVien(input().strip(),input().strip(),input().strip(),input().strip())
        a.append(sv)

    # Đọc số lượng truy vấn
    q = int(input())
    queries = [input().strip() for _ in range(q)]

    # Thực hiện truy vấn
    for lop_truy_van in queries:
        print(f'DANH SACH SINH VIEN LOP {lop_truy_van} :')
        for sv in a:
            if sv.lop == lop_truy_van:
                print(sv)
