class SinhVien:
    def __init__(self, ma, ten, lop, email):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email

    def get_khoa(self):
        return self.ma[:4]

    def chuanhoa_ten(self):
        name = self.ten.strip().split()
        self.ten = ' '.join(word.title() for word in name)

    def __str__(self):
        self.chuanhoa_ten()  # Chuẩn hóa tên khi in
        return f'{self.ma} {self.ten} {self.lop} {self.email}'


if __name__ == '__main__':
    # Đọc danh sách sinh viên
    n = int(input())
    a = []
    for _ in range(n):
        sv = SinhVien(input().strip(), input().strip(), input().strip(), input().strip())
        a.append(sv)

    # Đọc số lượng truy vấn
    q = int(input())
    queries = [input().strip() for _ in range(q)]

    # Thực hiện truy vấn
    for khoa_truy_van in queries:
        print(f'DANH SACH SINH VIEN KHOA {khoa_truy_van} :')
        for sv in a:
            if sv.get_khoa() == khoa_truy_van:
                print(sv)
