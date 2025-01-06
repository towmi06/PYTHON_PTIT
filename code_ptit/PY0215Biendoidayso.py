while True:
    a = [int(x) for x in input().split()]
    if a == [0, 0, 0, 0]:  # Điều kiện dừng
        break
    else:
        steps = 0
        while len(set(a)) > 1:  # Kiểm tra xem các phần tử có giống nhau hay không
            steps += 1
            # Tạo dãy mới từ hiệu các phần tử liên tiếp
            new= [abs(a[i] - a[i+1]) for i in range(3)]
            new.append(abs(a[3] - a[0]))
            a = new
        print(steps)
