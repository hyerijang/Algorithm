# https://programmers.co.kr/learn/courses/30/lessons/77485
# * 정답 (40분)
# 쉽넹

import collections


def get_right_index(query):
    x1, y1, x2, y2 = query
    return x1-1, y1-1, x2-1, y2-1


def rotate(board, query):
    x1, y1, x2, y2 = get_right_index(query)

    # 회전에 의해 위치 변경되는 값들 추출
    q = []
    for y in range(y1, y2+1):
        q.append(board[x1][y])

    for x in range(x1+1, x2+1):
        q.append(board[x][y2])

    for y in range(y2-1, y1, -1):
        q.append(board[x2][y])

    for x in range(x2, x1, -1):
        q.append(board[x][y1])

    # 회전
    q = collections.deque([q[-1]] + q[:-1])
    min_value = min(q)

    # 갱신
    for y in range(y1, y2+1):
        board[x1][y] = q.popleft()

    for x in range(x1+1, x2+1):
        board[x][y2] = q.popleft()

    for y in range(y2-1, y1, -1):
        board[x2][y] = q.popleft()

    for x in range(x2, x1, -1):
        board[x][y1] = q.popleft()

    return min_value


def solution(rows, columns, queries):
    answer = []

    board = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]

    for query in queries:
        answer.append(rotate(board, query))

    return answer
