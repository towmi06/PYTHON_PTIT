myMap = set()
a = []

MAX_LIMIT = 10**18

# Sinh các số Hamming
for i in range(60):
    for j in range(38):
        for z in range(26):
            num = 2 ** i * 3 ** j * 5 ** z
            if num > MAX_LIMIT:
                break  # Ngừng nếu số vượt quá giới hạn
            myMap.add(num)

# Chuyển đổi set thành danh sách và sắp xếp
a = sorted(myMap)

# Hàm tìm kiếm nhị phân
def binSearch(l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x: return mid + 1  # Trả về thứ tự (bắt đầu từ 1)
        elif a[mid] < x: l = mid + 1
        else: r = mid - 1
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    idx = binSearch(0, len(a) - 1, n)
    if idx == -1: print("Not in sequence")
    else:  print(idx)