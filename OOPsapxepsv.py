import sys
# khong biet so luong sinh vien
class SinhVien:
    def __init__(self, ma, ten, lop, email):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email

    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.email}'

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')  # Đọc toàn bộ dữ liệu đầu vào
    n = len(data) // 4  # Tính số sinh viên
    a = []

    # Xử lý dữ liệu cho từng sinh viên
    for i in range(n):
        ma = data[i * 4].strip()
        ten = data[i * 4 + 1].strip()
        lop = data[i * 4 + 2].strip()
        email = data[i * 4 + 3].strip()
        sv = SinhVien(ma, ten, lop, email)
        a.append(sv)

    # Sắp xếp theo lớp và mã sinh viên
    a.sort(key=lambda x: (x.ma))

    # In danh sách sau khi sắp xếp
    for sv in a:
        print(sv)
'''
data[i * 4]

data là danh sách chứa toàn bộ dữ liệu đầu vào, mỗi dòng được lưu là một phần tử trong danh sách này (giả sử đã đọc qua input() và tách bằng cách sử dụng .splitlines()).
Do mỗi sinh viên được mô tả bằng 4 dòng, sinh viên thứ i sẽ bắt đầu từ dòng thứ i * 4:
Dòng đầu tiên data[i * 4] là mã sinh viên.
data[i * 4 + 1]: Đây là dòng thứ hai chứa họ và tên.
data[i * 4 + 2]: Dòng thứ ba chứa lớp học.
data[i * 4 + 3]: Dòng thứ tư chứa email.
.strip(): loại bỏ mọi ký tự khoảng trắng dư thừa ở đầu và cuối mỗi dòng dữ liệu.
'''