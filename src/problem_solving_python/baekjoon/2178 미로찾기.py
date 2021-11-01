# https://www.acmicpc.net/status?user_id=chjang5621&problem_id=2178&from_mine=1
# * 정답(50분)
# - 경로 길이 저장을 어케하나 기억이 안나서 오래걸림
# - 입출력도.. 오랜만에 하니까 헷갈리넹
# - 평범한 BFS 문제. 다음에 풀면 더 잘 풀 수 있을 듯.


# [내코드]
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def is_in_range(x, y):
    if x in range(n) and y in range(m):
        return True

    return False


def bfs(graph, start, visited):

    queue = deque()

    x = start[0] - 1
    y = start[1] - 1

    visited[x][y] = 1
    queue.append((x, y))

    while queue:
        next = queue.popleft()
        x, y = next[0],  next[1]
        # 상하좌우 검사하기
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if is_in_range(new_x, new_y) and graph[new_x][new_y]:
                if not visited[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y] + 1
                    queue.append((new_x, new_y))

                    # 목표지점에 도달하면 종료
                    if (new_x, new_y) == target:
                        print(visited[new_x][new_y])
                        return

    return


def main():
    # 입력
    global n, m
    n, m = map(int, input().split())

    # 목표지점
    global target
    target = (n-1, m-1)

    # '길'이면 True 아니면 False
    graph = [[True if i == '1' else False for i in list(
        input())] for _ in range(n)]

    visited = [[0 for _ in range(m)] for _ in range(n)]

    bfs(graph, (1, 1), visited)


if __name__ == "__main__":
    main()
