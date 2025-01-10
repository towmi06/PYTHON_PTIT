from collections import deque

def bfs(matrix, N, M):
    directions = [(1, 0), (0, 1), (1, 1)]  # Các hướng di chuyển
    queue = deque([(0, 0)])  # Hàng đợi BFS, bắt đầu từ vị trí A[1][1]
    steps = [[float('inf')] * M for _ in range(N)]  # Mảng lưu số bước đi ít nhất
    steps[0][0] = 0  # Số bước đi từ A[1][1] đến chính nó là 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                cost = abs(matrix[nx][ny] - matrix[x][y])
                if steps[nx][ny] > steps[x][y] + cost:
                    steps[nx][ny] = steps[x][y] + cost
                    queue.append((nx, ny))

    return steps[N-1][M-1] if steps[N-1][M-1] != float('inf') else -1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(matrix, N, M)
    print(result)