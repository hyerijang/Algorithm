# https://programmers.co.kr/learn/courses/30/lessons/12903
# * 정답 (10분)
# - 쉬운데 꽤 오래걸린 편..

def solution(s):
    mid = len(s) // 2
    print(mid)
    if len(s) % 2 == 1:  # 단어의 길이가 홀수
        return s[mid]
    return s[mid-1:mid+1]


solution("abcde")
