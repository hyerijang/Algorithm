# https://programmers.co.kr/learn/courses/30/lessons/77484
# * 정답 (20분)
# - 문제 풀 때 범위 처리 똑바로 할것!
# - 테스트 케이스 하나가 계속 틀려서 질문하기 보고 해결함

def solution(lottos, win_nums):
    # 오름차순 정렬
    lottos.sort()
    win_nums.sort()

    lowest_rank = 7  # 0개 번호 일치
    print(lottos, win_nums)
    count_zero = 0
    for my_num in lottos:
        if my_num == 0:
            count_zero += 1
            continue
        if my_num in win_nums:
            lowest_rank -= 1
            win_nums.remove(my_num)  # 이미 고른 번호는 삭제

    highest_rank = lowest_rank - count_zero

    if lowest_rank >= 6:  # 7순위는 존재하지 않으므로 최저 순위인 6으로 변경
        lowest_rank = 6
    if highest_rank < 1:  # 1보다 높은 순위는 x
        highest_rank = 1
    if highest_rank >= 6:  # 7순위는 존재하지 않으므로 최저 순위인 6으로 변경
        highest_rank = 6
    print([highest_rank, lowest_rank])
    return [highest_rank, lowest_rank]


lottos = [[44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0],
          [45, 4, 35, 20, 3, 9], [1, 2, 3, 4, 5, 6]]
win_nums = [[31, 10, 45, 1, 6, 19],
            [38, 19, 20, 40, 15, 25],
            [20, 9, 3, 45, 4, 35],
            [7, 8, 9, 10, 11, 12]]

result = [[3, 5], [1, 6], [1, 1], [6, 6]]


for i in range(len(lottos)):
    print(solution(lottos[i], win_nums[i]) == result[i])
