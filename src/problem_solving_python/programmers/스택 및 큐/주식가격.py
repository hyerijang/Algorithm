# https://programmers.co.kr/learn/courses/30/lessons/42584
# [Level 2]
# *정답(30분) : 설계 10, 코딩 20
# - 문제 분류가 스택/큐인게 보여서 쉽게 풀었는데... 안보였으면 효율성테스트에서 갈려나갔을듯.

sec = 0
price = 1


def solution(prices):
    # li 는 (시각, 가격)으로 이루어진 튜플로 구성
    # 편의상 시각은 0초부터 시작
    li = list(enumerate(prices))
    stack = []
    answer = [0] * len(prices)

    for data in li:
        if stack == []:
            stack.append(data)
            continue

        # stack 에 자료가 남아있는 동안
        # 가격이 떨어진 경우 해당 튜플을 stack에서 pop
        while stack != [] and stack[-1][price] > data[price]:
            # 가격이 현재와 동일하거나 이전보다 높아진 경우만 스택에 남게 되므로
            # 스택은 늘 가격순으로 정렬되어 있는 상태로 유지된다
            drop_rec = stack.pop()
            # 떨어지기 까지 얼마나 걸렸는지 기록
            answer[drop_rec[sec]] = data[sec] - drop_rec[sec]

        # 현재 데이터를 스택의 끝에 추가
        stack.append(data)

    # 스택에 데이터가 남아있는 경우 끝까지 가격이 떨어지지 않은 것이므로 이를 기록
    for data in stack:
        answer[data[sec]] = len(prices) - data[sec] - 1

    return answer
