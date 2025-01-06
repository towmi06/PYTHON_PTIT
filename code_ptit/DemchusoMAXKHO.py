def count_digits(n):
    """
    Đếm số lần xuất hiện của các chữ số từ 0 đến 9 trong các số từ 1 đến n.
    """
    cnt = [0] * 10  # Mảng lưu số lần xuất hiện của các chữ số từ 0 đến 9.
    if n == 0:
        return cnt  # Nếu n = 0, trả về mảng toàn 0.

    power = 1  # Biến đại diện cho 10^k (vị trí chữ số đang xét).
    while power <= n:
        higher = n // (power * 10)  # Các số ở hàng lớn hơn.
        current = (n // power) % 10  # Chữ số hiện tại đang xét.
        lower = n % power  # Các số ở hàng nhỏ hơn.

        # Cộng số lần xuất hiện từ các chữ số ở hàng lớn hơn:
        # Mỗi chữ số xuất hiện "higher * power" lần.
        for digit in range(10):
            cnt[digit] += higher * power

        # Cộng thêm số lần xuất hiện của các chữ số nhỏ hơn chữ số hiện tại:
        for digit in range(current):
            cnt[digit] += power

        # Cộng thêm số lần xuất hiện của chữ số hiện tại:
        cnt[current] += lower + 1

        # Trừ số lần xuất hiện không hợp lệ của chữ số 0 ở các vị trí cao nhất:
        # Vì số 0 không được tính ở hàng cao nhất khi viết số.
        cnt[0] -= power

        # Chuyển sang vị trí chữ số tiếp theo (10^k -> 10^(k+1)).
        power *= 10

    return cnt


if __name__ == '__main__':
    T = int(input())  # Số lượng bộ test.
    results = []  # Danh sách lưu kết quả cho từng test case.
    for _ in range(T):
        A, B = map(int, input().split())
        # Đếm số lần xuất hiện của các chữ số từ 1 -> B.
        cnt_B = count_digits(B)
        # Đếm số lần xuất hiện của các chữ số từ 1 -> A-1 (nếu A > 1).
        cnt_A_minus_1 = count_digits(A - 1) if A > 1 else [0] * 10
        # Tính số lần xuất hiện trong khoảng A -> B:
        # Lấy hiệu giữa kết quả từ 1 -> B và 1 -> A-1.
        result = [cnt_B[i] - cnt_A_minus_1[i] for i in range(10)]
        # Chuyển kết quả thành chuỗi và thêm vào danh sách kết quả.
        results.append(" ".join(map(str, result)))

    # In tất cả kết quả cho các bộ test.
    print("\n".join(results))
