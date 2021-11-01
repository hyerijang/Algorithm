# https://programmers.co.kr/learn/courses/30/lessons/12977
# * 정답 (20분)
# - 소수랑 조합 쓰면 되게 쉽게 푸는데 내가 기억을 못해서 찾아가면서 푸느라 20분 걸림

from itertools import combinations

# 소수 판별 함수(2이상의 자연수에 대하여)


def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(nums):

    answer = 0
    candidates = list(combinations(nums, 3))
    # print(candidates)
    for c in candidates:
        if is_prime_number(sum(c)):
            answer += 1

    return answer


solution([1, 2, 3, 4])
