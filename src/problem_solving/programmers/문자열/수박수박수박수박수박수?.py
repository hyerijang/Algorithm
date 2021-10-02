# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
# * 정답 (5분 미만)
# - 정말 파이썬다운 코드가 있어서 아래에 기록해둠!

def water_melon(n):
    s = "수박" * n
    return s[:n]


# - 내풀이
pattern = "수박"


def solution(n):
    answer = ''

    answer = pattern * (n//2)
    if n % 2 == 1:
        answer += '수'

    return answer


solution(3)
