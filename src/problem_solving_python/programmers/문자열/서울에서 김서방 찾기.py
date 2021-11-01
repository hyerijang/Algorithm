# https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3
# * 정답 (5분 미만)
# - 새로운 함수 index 쓴 예시  알게되서 기록해둠
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


def solution(seoul):
    list = []
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"


seoul = ["Jane", "Kim"]

print(solution(seoul))
