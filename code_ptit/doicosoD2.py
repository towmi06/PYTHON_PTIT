from math import log2

f = '0123456789ABCDEF'  # Hệ ký tự trong các cơ số
if __name__ == '__main__':
    t = int(input())  
    for _ in range(t):
        coso = int(input()) 
        x = input() 
        # Tính số bit cần để biểu diễn một ký tự
        so_bits = int(log2(coso))
        # Thêm các số '0' vào đầu để độ dài chia hết cho so_bits
        while len(x) % so_bits != 0:
            x = '0' + x
        # Chuyển đổi từng nhóm so_bits thành ký tự
        for i in range(0, len(x), so_bits):
            s = 0
            for j in range(i, i + so_bits):
                s = s * 2 + int(x[j])  # Tính giá trị thập phân
            print(f[s], end='')  # In ký tự tương ứng
        print()
