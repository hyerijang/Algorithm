import sys

answer = 0

def list_to_str(li:list):
    return "".join(li)




def dfs(number_board,count,visited):

    global  answer
    key = list_to_str(number_board)

    if count == 0:
        if answer < int(key):
            answer = int(key)
        return

    visited[(key,count)] = True #방문표시

    for i in range(len(number_board)):
        for j in range(i,len(number_board)):
            number_board[i] ,number_board[j] = number_board[j],number_board[i]
            key = list_to_str(number_board)
            if not visited.get((key, count)):
                visited[(key, count)] = True
                dfs(number_board,count-1,visited)
            number_board[i] ,number_board[j] = number_board[j],number_board[i]

    return




def simulation():
    sys.stdin = open("input.txt", "r")

    n = int(input())  # 테스트 케이스 입력 개수
    tc_list = [list(map(int, input().split())) for _ in range(n)]  # 테스트케이스


    for i in range(len(tc_list)):
        number, count = tc_list[i]
        number_board = [str(x) for x in str(number)]
        # print(list_to_int(number_board), count)

        global answer
        answer = 0

        visited = {}

        dfs(number_board,count,visited)
        print(f"#{i+1} {answer}" )




simulation()