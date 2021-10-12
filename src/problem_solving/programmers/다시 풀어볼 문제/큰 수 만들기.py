
# ! 틀림 (1시간)
# https://programmers.co.kr/learn/courses/30/lessons/42883#


# [모범답안]
# https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC


# [내 풀이]
# -조합으로 풀었음. 쉬운 풀이지만 이렇게 풀면  100 퍼 시간초과 난다.

# 시간초과
from itertools import combinations


def solution(number, k):
    c = list(combinations(number, len(number)-k))
    # 가장 큰 값 리턴
    return "".join(list(max(c)))
