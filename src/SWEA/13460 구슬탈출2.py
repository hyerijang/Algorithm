# https://www.acmicpc.net/problem/13460
# 2022-01-07

# ! 틀림 (1시간)
# 틀린 이유
# 1. BFS 인걸 눈치도 못챔 (재귀함수로 풀려고 했음... 그거 아니야... )
# 2. 구슬 움직이는 걸 어떻게 처리해야 할 지 감 못잡음
#   2-1. 특히 빨간 구슬이랑 파란 구슬을 겹칠 때, 이걸 어떻게 처리해야하는지
# 3. 게임판을 기울이고 나서, 게임판을 update함.
#   3-1 판을 수정하면 안됨...


# [모범답안]
# https://seoyoung2.github.io/algorithm/2020/06/18/Baekjoon-13460.html

# 틀린 이유
# - 1. BFS
#   1-1. visited (dict): key = 빨간공,파란공의 좌표 , value = 좌표가 그러할 때, 최소 이동 횟수
#   1-2. visited 하지 않은 빨공파공 좌표는 다음 탐색을 위해 queue에 넣는다.
# - 2. 구슬 움직이기 (movemove 함수, 상대좌표 사용, 이동거리 저장)
#   2-1. 빨간 구슬이랑 파란 구슬을 겹치는 경우를 처리하기 위해 이동 거리(move) 를 저장한다.
#        이동 거리가 더 짧은 구슬이 해당 좌표에 더 먼저 도착한 구슬이므로 긴 구슬은 한칸 이전으로 돌아간다.
# - 3. 구슬의 위치에 따라 최소 기울임 횟수를 visited에 저장한다. (1-1 참조)

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            red = [i, j]
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            blue = [i, j]


def movemove(x, y, dx, dy):
    move = 0  # !구슬이 움직인 횟수
    while graph[x+dx][y+dy] != '#':
        # 구멍으로 탈출할 경우 0,0 return
        if graph[x+dx][y+dy] == 'O':
            return 0, 0, 0
        x += dx
        y += dy
        move += 1
    return x, y, move


def bfs():
    # !빨간 구슬과 파란 구슬 동시에 방문체크 해야함
    visit = {}  # dict
    queue = deque([red + blue])  # !BFS
    visit[red[0], red[1], blue[0], blue[1]] = 0  # 방문

    # BFS 탐색 시작
    while queue:
        rx, ry, bx, by = queue.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):      # 상하좌우
            nrx, nry, rmove = movemove(rx, ry, dx, dy)
            nbx, nby, bmove = movemove(bx, by, dx, dy)

            # - 두 공 모두 또는 파란 공만 탈출한 경우 (실패)
            if not nbx and not nby:
                continue
            # [종료조건] 빨간 공만 탈출한 경우 (성공)
            elif not nrx and not nry:
                print(visit[rx, ry, bx, by] + 1)
                return

            # ! 두 공이 같은 위치에 있는 경우
            elif nrx == nbx and nry == nby:
                # 이동거리가 적은 구슬을 한 칸 뒤로
                if rmove > bmove:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            # visit하지 않았으면 queue에 append
            if (nrx, nry, nbx, nby) not in visit:
                visit[nrx, nry, nbx, nby] = visit[rx, ry, bx, by] + 1
                queue.append([nrx, nry, nbx, nby])

        # [종료조건]  answer에 값을 넣었거나 queue가 비었거나 움직인 횟수가 10이상이면 그만
        if not queue or visit[rx, ry, bx, by] >= 10:
            print(-1)
            return


bfs()
