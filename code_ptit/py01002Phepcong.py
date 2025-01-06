# Nhập một chuỗi từ người dùng và loại bỏ khoảng trắng ở đầu và cuối chuỗi
s = input().strip()

# Tách phần đầu tiên trước dấu '+' và chuyển nó thành số nguyên (giá trị của a)
a = int(s.split('+')[0])

# Tách phần thứ hai sau dấu '+' (bao gồm cả phần '=') và tiếp tục tách trước dấu '=' để lấy giá trị b
b = int(s.split('+')[1].split('=')[0])

# Tách phần sau dấu '=' và chuyển nó thành số nguyên (giá trị của c)
c = int(s.split('=')[1])

print('YES' if a + b == c else 'NO')
