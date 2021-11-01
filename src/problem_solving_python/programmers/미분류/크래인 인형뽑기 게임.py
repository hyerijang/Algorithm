# https://programmers.co.kr/learn/courses/30/lessons/64061
# 30분 소요 (정답)

basket = []  # 스택


def solution(board, moves):
    answer = 0

    # 인형 옮기기
    for m in moves:
        for i in range(len(board)):
            doll = board[i][m-1]
            if doll != 0:  # m번 칸에 인형있으면
                # 게임판에서 인형 뺌
                board[i][m-1] = 0
                # print(basket, doll, "위치:", m)

                # 바구니에 인형이 없는 경우
                if len(basket) == 0:
                    basket.append(doll)

                else:
                    last_puppet = basket.pop()
                    if last_puppet != doll:
                        basket.append(last_puppet)
                        basket.append(doll)
                    else:
                        # print("터트림")
                        answer += 2
                break

    return answer


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
