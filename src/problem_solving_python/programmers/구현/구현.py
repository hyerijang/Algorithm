# https://programmers.co.kr/learn/courses/30/lessons/17680
# [Level2]
# * 정답 (30분)
# - 어렵지는 않았음.

# [내 풀이]
# 캐시 사이즈는 0개 이상 30개 이하
# 최대 도시 수는 10만개
# 도시 이름은 영문자로만 구성: 대소문자 구분을 하지 않으므로 소문자로 전부 통일할 것

# 캐시 교체 알고리즘 : LRU
# 캐시는 큐로 구현
# left : 가장 마지막으로 사용 (교체 대상)
# right : 가장 최근 사용

from collections import deque
cache = deque()

hit = True
miss = False


def is_hit(cache, city):
    if city in cache:
        return hit

    return miss


def replace(cahce, cacheSize, city):
    # leftpop 후 city 주입.
    if cacheSize:
        if len(cache) == cacheSize:
            cache.popleft()
        cache.append(city)
    return


def solution(cacheSize, cities):

    cities = list(map(lambda x: x.lower(), cities))
    time = 0

    for city in cities:
        # hit인경우
        if is_hit(cache, city):
            time += 1  # 1초 추가
            # 꺼내서 맨 뒤으로 보냄
            cache.remove(city)
            cache.append(city)
            continue
        # False인 경우
        else:
            time += 5  # 5초 추가
            replace(cache, cacheSize, city)

    return time
