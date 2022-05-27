# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# 1220. [S/W 문제해결 기본] 5일차 - Magnetic

EMPTY = 0
N = 1
S = 2

for case in range(10):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]

    answer = 0


    def move(board, y, x, dir):
        board[y + dir][x] = board[y][x]
        board[y][x] = EMPTY


    # 자기장 걸기 (1칸씩 이동)
    def move_all_magnet(board):

        자성체이동 = False

        # 1. N극 자성체 아래로 1칸씩 이동
        dy = 1  # 방향
        for y in range(size)[::-1]:
            for x in range(size)[::-1]:
                if board[y][x] == N:
                    ny = y + dy
                    if ny < size and board[ny][x] == EMPTY:  # 다음칸 있고 비어있음
                        move(board, y, x, dy)
                        자성체이동 = True
                    elif ny == size:  # 다음칸 없음 떨어짐
                        board[y][x] = EMPTY
                        자성체이동 = True

        # 2. S극 자성체 위로 1칸씩 이동
        dy = -1  # 방향
        for y in range(size):
            for x in range(size):
                if board[y][x] == S:
                    ny = y + dy
                    if 0 <= ny and board[ny][x] == EMPTY:  # 다음칸 있고 비어있음
                        move(board, y, x, dy)
                        자성체이동 = True
                    elif ny == -1:  # 다음칸 없으면 떨어짐
                        board[y][x] = EMPTY
                        자성체이동 = True

        return 자성체이동


    자성체이동가능 = True
    while 자성체이동가능:
        자성체이동가능 = move_all_magnet(board)


    def 교착상태카운트(board: list):
        count = 0
        size = len(board)
        visited = [[False for _ in range(size)] for _ in range(size)]

        for y in range(size):
            for x in range(size):
                if not visited[y][x] and board[y][x] == N:  # 교착상태 시작
                    count += 1
                    ny = y
                    while board[ny][x] != S:
                        visited[ny][x] = True
                        ny += 1

        return count


    answer = 교착상태카운트(board)

    print(f"#{case + 1} {answer}")
