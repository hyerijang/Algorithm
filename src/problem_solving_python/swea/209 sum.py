# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# 209. [S/W 문제해결 기본] 2일차 - Sum


for _ in range(10):
    case = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]  # 100 x 100

    # 1. 각 행의 합
    sum_of_row = max([sum(array[row]) for row in range(100)])

    # 2. 각 열의 합
    sum_of_column = max([sum([array[row][column] for row in range(100)]) for column in range(100)])

    # 3. 대각선 (\)
    sum_of_diagonal = sum([array[row][row] for row in range(100)])

    # 4. 대각선 (/)
    sum_of_diagonal2 = sum([array[row][100 - row - 1] for row in range(100)])

    print(f"#{case} {max(sum_of_row, sum_of_column, sum_of_diagonal, sum_of_diagonal2)}")
