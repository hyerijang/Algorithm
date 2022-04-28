# https://www.acmicpc.net/status?user_id=chjang5621&problem_id=16234&from_mine=1
# ! 시간초과
# - 내 풀이의 경우 연합국 대상을 찾는 과정에서 불필요한 반복 있었던거 같음

# [내 풀이]
from collections import deque
from ctypes import Union
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]


NOTUNION = -1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[NOTUNION for _ in range(n)]
           for _ in range(n)]  # 연합 번호는 0번부터 시작

unions = {}
p_unions = {}
union_num = 0
nation_not_in_union = True


def find_not_union(visited):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == NOTUNION:
                return (i, j)

    return False


def bfs(start):

    global a, unions, visited, union_num, p_unions

    # start 국가와 같은 연합이 될 수 있는 국가를 탐색
    y = start[0]
    x = start[1]

    # 연합 생성
    unions[union_num] = [(y, x)]
    visited[y][x] = union_num
    p_unions[union_num] = a[y][x]

    q = deque()
    q.append((y, x))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 > ny or 0 > nx or n == ny or n == nx:
                continue

            if visited[ny][nx] == NOTUNION:  # 이번에 방문한 국가가 다른 연합에 속한 국가가 아니라면
                diff = abs(a[y][x] - a[ny][nx])  # 국경선을 공유할 수 있는 국가인지 체크
                if l <= diff <= r:
                    visited[ny][nx] = union_num
                    q.append((ny, nx))
                    p_unions[union_num] += a[ny][nx]
                    unions[union_num].append((ny, nx))
                if diff > 0:
                    global is_all_same
                    is_all_same = False


def solution():
    day = 0

    global is_all_same, unions, visited, union_num, p_unions

    while day <= 2000:
        is_all_same = True
        # 0. 해당 일자의 연합 초기화
        visited = [[NOTUNION for _ in range(n)]
                   for _ in range(n)]  # 연합 번호는 0번부터 시작

        unions = {}
        p_unions = {}
        union_num = 0
        nation_not_in_union = True

        # 1. bfs로 연합인 나라 구하기
        while True:
            nation_not_in_union = find_not_union(visited)
            if nation_not_in_union == False:
                break
            else:
                union_num += 1
                bfs(nation_not_in_union)

        # 2.1 만약 연합이 1개이고 모든 인구가 동일한 경우
        # =>  인구이동 발생 X => 종료
        if len(unions.keys()) == 1 and is_all_same:
            break

        if len(unions.keys()) == n*n:  # 2.1 국경선이 열릴 수 있는 국가가 없는 경우
            break

        day += 1
        # 3. 각 연합들의 인구 수 업데이트
        for un in unions.keys():  # un : 연합 번호
            size = len(unions[un])  # 연합 크기
            avg_population = p_unions[un]//size  # 연합 평균 인구수
            for loc in unions[un]:
                a[loc[0]][loc[1]] = avg_population

    return day


print(solution())

# [모범답안]
# https://ryu-e.tistory.com/40
# import sys
# import math
# from collections import deque

# # 남 동 북 서
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# n, l, r = map(int, sys.stdin.readline().split())  # n*n, 인구차이 l명 이상, r명 이하

# arr = list()
# a_list = list()
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))


# def bfs(i, j):
#     dq = deque()
#     dq.append((i, j))
#     visit[i][j] = True
#     # 연합된 국가 담기
#     union = [(i, j)]
#     count = arr[i][j]   # 총 연합된 국가 수
#     # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기
#     while dq:
#         x, y = dq.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             if visit[nx][ny]:
#                 continue
#             if l <= abs(arr[nx][ny] - arr[x][y]) <= r:  # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기
#                 union.append((nx, ny))
#                 visit[nx][ny] = True
#                 dq.append((nx, ny))
#                 count += arr[nx][ny]
#     # 2. 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 되도록 계산
#     for x, y in union:
#         arr[x][y] = math.floor(count / len(union))

#     return len(union)


# result = 0    # 인구 이동이 발생하는 일수
# while True:   # 1. 인구 이동이 없을 때까지 반복
#     visit = [[False] * n for _ in range(n)]
#     flag = False  # 인구 이동 존재 유무 플래그
#     # 2. 모든 곳을 bfs로 방문하여 연합 진행
#     for i in range(n):
#         for j in range(n):
#             if not visit[i][j]:
#                 if bfs(i, j) > 1:
#                     flag = True
#     if not flag:   # 3. 지금까지 인구 이동이 없는 경우, 그만
#         break
#     result += 1

# print(result)
