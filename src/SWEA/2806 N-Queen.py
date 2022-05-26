# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
# 2806. N-Queen (D3)
from copy import deepcopy

t = int(input())

OK = 0
QUEEN = 9
CANT = 1


def 같은열표시(next_board: list, queen: tuple):
    qy = queen[0]
    next_board[qy] = [QUEEN if next_board[qy][j] == QUEEN else CANT for j in range(len(board))]  # 같은 열
    return


def 같은행표시(next_board: list, queen: tuple):
    qx = queen[1]
    for y in range(len(next_board)):
        next_board[y][qx] = QUEEN if next_board[y][qx] == QUEEN else CANT
    return


def 대각선표시(next_board: list, queen: tuple):
    qy, qx = queen
    n = len(next_board)
    # 대각선(우상향)
    for d in range(-n, n):
        ny, nx = qy + d, qx + d
        if 0 <= ny < n and 0 <= nx < n:
            if next_board[ny][nx] != QUEEN:
                next_board[ny][nx] = CANT

    # 대각선(우하향)
    for d in range(-n, n):
        ny, nx = qy - d, qx + d
        if 0 <= ny < n and 0 <= nx < n:
            if next_board[ny][nx] != QUEEN:
                next_board[ny][nx] = CANT

    return


def 놓을수있는열개수(next_board, ):
    count = 0
    for li in next_board:
        if OK in li:
            count += 1
    return count


def set_board(board, start, left_piece):
    n = len(board)

    if left_piece == 0:  # n번 ~ 1번 체스퀸 다 놓았으면
        return 1

    result = 0

    i, j = start

    for nx in range(n):
        if board[i][nx] == OK:
            next_board = deepcopy(board)
            next_board[i][nx] = QUEEN
            queen = (i, nx)

            같은열표시(next_board, queen)
            같은행표시(next_board, queen)
            대각선표시(next_board, queen)

            if 놓을수있는열개수(next_board) == left_piece - 1:
                next = (i+ 1, 0)
                result += set_board(next_board, next, left_piece - 1)

    return result


for case in range(t):
    n = int(input())
    answer = 0

    board = [[0 for _ in range(n)] for _ in range(n)]

    answer = set_board(board, (0, 0), n)

    print(f"#{case + 1} {answer}")
