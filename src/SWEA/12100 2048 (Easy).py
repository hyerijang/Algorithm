
# https://www.acmicpc.net/problem/12100
# ! 실패 (1시간 30분) - 풀다가 포기함
'''
틀린 이유?
    1. 문제를 제대로 안읽음
    2. DFS로 풀어야 된대. BFS 아니었음
    3. board를 copy 해서 풀 수 있는 거였는데 안될거라고 지레 짐작하고 일을 더 복잡하게 만듦
    4. deppcopy를 몰랐음
    5. 같은 줄이더라도 어느 방향으로 미느냐에 따라 다른 결과 나올 수 있음.
        => 미는 방향을 4개로 해서 각각마다 다른 로직을 짜는 것 보단
        => 미는 방향은 1가지로 하고 *판을 회전*시키는게 편함
'''

# [모범답안]
# - 블록을 상하좌우로 이동하는 방법이 아닌, 보드를 90도 돌리고 무조건 왼쪽으로 합치는 방법
from copy import deepcopy

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]


# rotate : 보드를 90도 회전시킴
def rotate(N, B):
    new_lst = deepcopy(B)
    for i in range(N):
        for j in range(N):
            new_lst[j][N-i-1] = B[i][j]
    return new_lst


# convert : list에서 같은값이 있다면 왼쪽으로 이동시켜서 합침
def convert(N, B):
    new_lst = [i for i in B if i != 0]  # 0을 제외한 list저장
    for i in range(1, len(new_lst)):
        if new_lst[i-1] == new_lst[i]:
            new_lst[i-1] *= 2
            new_lst[i] = 0
    new_lst = [i for i in new_lst if i != 0]
    return new_lst + [0]*(N-len(new_lst))  # list길이만큼 오른쪽에 0추가


# dfs : 보드에서 최댓값을 저장하고 convert, rotate함수를 부름
def dfs(N, B, count):
    # 현재 보드에서 가장 큰 값 찾기
    result = max([max(i) for i in B])
    if count == 0:
        return result

    # 회전
    for _ in range(4):
        C = [convert(N, i) for i in B]  # list한줄씩 변환한뒤 합침
        result = max(result, dfs(N, C, count-1))
        B = rotate(N, B)  # 회전
    return result


print(dfs(N, Board, 5))


# [내 풀이] - 실패 , (220108)
'''
# 입력 및 초기화

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


# [numbrs]
# - key :각 숫자의 위치 좌표
# - value : 해당 좌표의 숫자

graph = dict()

for y in range(n):
    for x in range(n):
        if board[y][x] != 0:
            graph[(y, x)] = board[y][x]

print(graph)


def movemove(y: int, x: int, dy: int, dx: int):
    tmp = graph[(y, x)]
    graph.pop((y, x))
    while y + dy in range(n) and x + dx in range(n):
        # 숫자 블록과 부딪친 경우
        if graph.get((y+dy, x+dx)) is not None:
            # 같은 숫자와 부딪친 경우
            if graph[(y+dy, x+dx)] == tmp:
                y += dy
                x += dx
                tmp = tmp * 2
                return y, x, tmp
            # 다른 숫자와 부딪친 경우
            else:
                return y, x, tmp

        else:
            y += dy
            x += dx

    # 어떤 블록과도 부딪치지 않고 벽에 닿음
    return y, x, tmp


for loc in tuple(graph.keys()):
    if graph.get(loc) is not None:
        ny, nx, tmp = movemove(loc[0], loc[1], 1, 0)
        graph[(ny, nx)] = tmp  # 갱신
        print(ny, nx, "=", tmp)
        print("그래프", graph)
'''
