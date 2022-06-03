# 프로그래머스 스킬테스트 3레벨 1번문제
# 처음에 그냥 무턱대고 작업 1개씩 돌리니까 시간초과 나더랑... 그래서 특정 작업량을 갖는 작업 개수(count)를 세서 한번에 빼버림

from collections import defaultdict


def solution(n, works):
    answer = 0
    time_counter = defaultdict(int)

    for w in works:
        time_counter[w] += 1

    while n:
        if not time_counter:
            break

        longest = max(time_counter.keys())

        # 가장 시간 많이 남은 작업을 처리
        count = time_counter[longest]  # 가장 오래걸리는 작업 개수

        if count == 0:
            break

        if count <= n:
            time_counter.pop(longest)
        else:
            count = n
            time_counter[longest] -= count

        if longest > 1:
            time_counter[longest-1] += count

        n -= count

    # 야근 지수 계산
    for time, x in time_counter.items():
        answer += (time*time) * x

    return answer
