if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    # Tìm giá trị tối ưu từ các giá trị ban đầu của dãy
    min_steps = float('inf')
    best_value = 0

    for x in a:
        steps = sum(abs(i- x) for i in a)  # Tính tổng khoảng cách tuyệt đối
        if steps < min_steps:  # Nếu tìm được tổng nhỏ hơn
            min_steps = steps
            best_value = x

    print(min_steps, best_value)
'''
8
13 5 8 7 9 15 26 34
59 13
'''