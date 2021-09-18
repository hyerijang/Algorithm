import re
import collections
from typing import Deque

s = input()
li = list(s)

# list로 구현


def solution(li):
    str = []
    for c in li:
        if c.isalnum:  # 만약 c가 영문자 or 숫자인 경우
            str.append(c.lower())

    while(len(str) > 1):
        if str.pop(0) != str.pop():
            return False
    return True

# 속도 개선 1
# deque로 구현
# popleft => O(1)
# def solution (li):
#     str : Deque = collections.deque()
#     for c in li :
#         if c.isalnum : #만약 c가 영문자 or 숫자인 경우
#             str.append(c.lower())

#     while(len(str) > 1):
#         if str.popleft() != str.pop():
#             return False
#     return True


# 속도 개선 2
# 문자열 슬라이싱 & 정규표현식
def solution(s):
    s = s.lower()  # 대문자를 소문자로 변경
    s = re.sub('[^a-z0-9]', '', s)  # s에서 a-z0-9이 아닌 문자열을 ''로 변경
    # re.sub（정규 표현식, 대상 문자열 , 치환 문자）
    # 정규 표현식 - 검색 패턴을 지정
    # 대상 문자열 - 검색 대상이 되는 문자열
    # 치환 문자 - 변경하고 싶은 문자
    # print(s)
    return s == s[::-1]


print(solution(s))
