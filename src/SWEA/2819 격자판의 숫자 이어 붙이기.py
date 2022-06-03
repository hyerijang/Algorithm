def dfs(start: tuple, board: list, word: list, words: dict):
    if len(word) == 7:
        words[str(word)] = True
        return

    absolute_coordinates = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    y, x = start
    for dy, dx in absolute_coordinates:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(board) and 0 <= nx < len(board):
            word.append(board[ny][nx])
            dfs((ny, nx), board, word, words)
            word.pop()


def get_seven_digits_num(board: list):
    words = {}

    for i in range(len(board)):
        for j in range(len(board)):
            start = (i, j)
            dfs(start, board, [board[i][j]], words)

    return len(words)


if __name__ == '__main__':

    t = int(input())

    for tc in range(t):
        board = [list(map(int, input().split())) for _ in range(4)]
        answer = get_seven_digits_num(board)
        print(f"#{tc + 1} {answer}")
