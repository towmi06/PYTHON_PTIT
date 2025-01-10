n = int(input())
a = [input().strip() for _ in range(n)]
cnt = 0

# Đếm số cặp 'C' trong từng hàng
for row in a:
    h = row.count('C')
    cnt += (h * (h - 1)) // 2

# Đếm số cặp 'C' trong từng cột
for col in range(n):
    c = sum(1 for row in a if row[col] == 'C')
    cnt += (c * (c - 1)) // 2

print(cnt)
