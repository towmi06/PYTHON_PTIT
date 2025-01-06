t = int(input().strip())

results = []
for _ in range(t):
    N = int(input().strip())
    
    power = 10
    
    while N >= power:
        # Tính phần dư (để xem xét làm tròn lên hay giữ nguyên)
        remainder = N % power
        
        # Nếu phần dư >= power / 2, làm tròn lên
        if remainder >= power // 2:
            N += power - remainder
        else:
            N -= remainder
        
        # Tăng bậc làm tròn (hàng chục -> hàng trăm -> hàng nghìn, ...)
        power *= 10
    
    results.append(N)

for res in results:
    print(res)
