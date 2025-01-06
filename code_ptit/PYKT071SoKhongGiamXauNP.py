import pickle
from collections import Counter

# Hàm kiểm tra số không giảm
def is_non_decreasing(num):
    s = str(num)
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))

# Đọc dữ liệu từ file nhị phân
def read_data(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

# Xử lý dữ liệu
data1 = read_data('DATA1.in')
data2 = read_data('DATA2.in')

# Lọc số không giảm và đếm số lần xuất hiện
counter1 = Counter([x for x in data1 if is_non_decreasing(x)])
counter2 = Counter([x for x in data2 if is_non_decreasing(x)])

# Lấy giao của các số không giảm
common_numbers = sorted(set(counter1.keys()) & set(counter2.keys()))

# Ghi kết quả
for num in common_numbers:
    print(num, counter1[num], counter2[num])
