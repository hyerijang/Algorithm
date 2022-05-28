# 복구 시간이 가장 짧은 경로에 대한 총 복구 시간
# 이동 시간은 고려 XX
from collections import deque

if __name__ == '__main__':

    t = int(input())

    for case in range(t):
        n = int(input())
        board = [list(map(int, list(input()))) for _ in range(n)]


        # 상하좌우 방향으로 움직일 수 있다.

        def bfs():
            total_cost = [[-1 for _ in range(n)] for _ in range(n)]

            q = deque()
            q.append((0, 0))
            total_cost[0][0] = 0

            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

            while q:
                y, x = q.popleft()
                for dy, dx in d:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n:

                        next_cost = total_cost[y][x] + board[ny][nx]
                        if total_cost[ny][nx] == -1 or total_cost[ny][nx] > next_cost:
                            total_cost[ny][nx] = next_cost  # 갱신
                            q.append((ny, nx))

            return total_cost, total_cost[-1][-1]


        total_cost, result = bfs()
        print(f"#{case + 1} {result}")
