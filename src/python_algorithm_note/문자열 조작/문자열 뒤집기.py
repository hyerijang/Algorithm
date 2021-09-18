import collections
from typing import Deque

s = input()

#list로 구현
def solution (s):
    li = list(s)
    li.reverse()
    return li
    
print(solution(s))

#슬라이싱으로 구현 (약간 더 빠름)
def solution2(s):
    rev = s[::-1]
    return rev
    
print(solution2(s))