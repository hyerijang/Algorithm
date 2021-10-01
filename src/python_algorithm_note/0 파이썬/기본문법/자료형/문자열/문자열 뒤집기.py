import collections
from typing import Deque

s = input()

# [방법1 ] list로 변환하여 뒤집기


def solution(s):
    li = list(s)
    li.reverse()
    return li


print(solution(s))

# [방법 2] 슬라이싱으로 뒤집기 (약간 더 빠름)


def solution2(s):
    rev = s[::-1]
    return rev


print(solution2(s))
