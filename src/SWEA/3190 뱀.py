from collections import deque


N = int(input())  # 보드 크기


def init_board(N):
    wall = -1
    board = [[0] * (N+1) for _ in range(N+1)]

    # 0번 행, 0번 열은 벽으로 간주
    board[0] = [wall] * (N+1)
    for y in range(N+1):
        board[y][0] = wall
    return board


board = init_board(N)

K = int(input())  # 사과 위치

for _ in range(K):
    y, x = map(int, input().split())
    board[y][x] = "A"

L = int(input())  # 뱀 방향 전환 횟수

dir_info = deque()
for _ in range(L):
    X, C = input().split()
    dir_info.append((int(X), C))


snake = deque()
snake.append((1, 1))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
head_dir = directions[0]


def turn(c):
    global head_dir
    idx = directions.index(head_dir)
    if c == 'L':  # 반시계방향으로 회전
        idx = idx-1
    else:
        idx = idx + 1
    head_dir = directions[idx]
    return directions[idx]


# head_dir = turn('L', head_dir)
# head_dir = turn('R', head_dir)


sec = 0


def is_out_of_range(t):
    for x in [0, 1]:
        if t[x] == 0 or t[x] > N:
            return True

    return False


def dfs(board,  snake, dir_info):
    # 방향 전환 정보 없음
    nt = 987654321

    if dir_info:
        nt, nd = dir_info.popleft()

    global sec

    # 다음 방향 전환 전까지 뱀 이동
    while sec < nt:
        sec = sec + 1
        # 뱀 머리 이동
        tmp = tuple(sum(elem) for elem in zip(snake[-1], head_dir))
        # print(sec, tmp)

        # 뱀의 몸이나 벽에 부딪치면 종료
        if tmp in snake:
            return

        if is_out_of_range(tmp):
            return

        snake.append(tmp)

        # 사과 못 먹은 경우
        if board[tmp[0]][tmp[1]] != "A":
            snake.popleft()  # 꼬리 회수

    turn(nd)
    dfs(board, snake, dir_info)


dfs(board, snake, dir_info)

print(sec)
