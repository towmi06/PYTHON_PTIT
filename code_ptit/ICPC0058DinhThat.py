from collections import deque

def check(n, k, u, v, ke):
    """
    Hàm kiểm tra xem đỉnh k có phải là đỉnh thắt giữa u và v không.
    - n: số lượng đỉnh trong đồ thị, m số cạnh .- k: đỉnh cần kiểm tra.
    - u: đỉnh bắt đầu.- v: đỉnh kết thúc.- ke: danh sách kề của đồ thị.
    """
    # Tạo hàng đợi cho BFS và mảng trạng thái để đánh dấu các đỉnh đã thăm
    queue = deque([u])  
    ok = [0] * (n + 1)  
    ok[u] = 1  # Đánh dấu đỉnh bắt đầu là đã thăm

    # Duyệt  BFS
    while queue:
        cur = queue.popleft()  # Lấy đỉnh hiện tại từ hàng đợi
        if cur == v:  # Nếu đến được đỉnh v, k không phải đỉnh thắt
            return False
        for i in ke[cur]:  # Duyệt các đỉnh kề của đỉnh hiện tại
            if not ok[i] and i != k:  # Chỉ duyệt đỉnh chưa thăm và không phải k
                queue.append(i)
                ok[i] = 1  
    return True  #  nên k là đỉnh thắt

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m, u, v = map(int, input().split())
        # Tạo danh sách kề
        ke = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            ke[x].append(y)
        # Đếm số đỉnh thắt
        cnt = 0
        for k in range(1, n + 1):  
            if k != u and k != v and check(n, k, u, v, ke):  
                # Nếu k không phải u hoặc v và là đỉnh thắt, tăng biến đếm
                cnt += 1
        print(cnt)
