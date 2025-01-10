import sys

def smallest_triplet_sum():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Số lượng test cases
    idx = 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])  # Số phần tử mảng
        idx += 1
        arr = map(int, data[idx:idx + n])  # Lấy mảng
        idx += n        
        # Ba số nhỏ nhất
        x = y = z = float('inf')
        
        for num in arr:
            if num < x:
                z, y, x = y, x, num
            elif num < y:
                z, y = y, num
            elif num < z:
                z = num
        
        results.append(x + y + z)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

