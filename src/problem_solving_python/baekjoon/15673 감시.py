# https://www.acmicpc.net/problem/15683
# ! 틀림
# - CCTV를 회전시키는 로직을 구현 안함... 왜그랬냐

# [내풀이]
from copy import deepcopy
import sys
from itertools import combinations_with_replacement
from typing import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
space = [list(map(int,  input().split())) for _ in range(n)]


def get_counter(space):
    counter = Counter()
    for i in range(n):
        counter += Counter(space[i])
    return counter


# CCTV의 개수 k, 벽의 개수 w
counter = get_counter(space)
k = counter[1] + counter[2] + counter[3] + counter[4] + counter[5]
w = counter[6]

# CCTV 방향 후보 : 중복조합으로 생성
cand = list(combinations_with_replacement(
    ([0, 1, 2, 3]), k))

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


WALL = 6
EMPTY = 0
WATCHING = -1

# CCTV 감시 범위 구하기
cctv_list = []
for y in range(n):
    for x in range(m):
        if 1 <= space[y][x] and space[y][x] <= 5:
            cctv_list.append((y, x))


def set_watches(loc: tuple, dir: int, space: list):

    ny = loc[0] + dy[dir]
    nx = loc[1] + dx[dir]

    while True:
        if ny < 0 or ny == n or nx < 0 or nx == m:
            break
        if space[ny][nx] == WALL:
            break

        if space[ny][nx] != WATCHING:
            space[ny][nx] = WATCHING

        ny = ny + dy[dir]
        nx = nx + dx[dir]


# 모드
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[1, 2, 3, 4]],
]


watches = 0

# k개의 감시카메라에 대하여 4방향 모두 시도
for c in cand:
    space_copy = deepcopy(space)
    for i in range(k):
        set_watches(cctv_list[i], c[i], space_copy)

    tmp = get_counter(space_copy)
    watches = max(watches, tmp[WATCHING])


print(n*m - k - w - watches)
