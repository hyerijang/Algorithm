# https://programmers.co.kr/learn/courses/30/lessons/42576
# [Level 1]
# * 정답 (24분)

# - 좋은 예시
# - collections의 Counter를 사용하면 리스트내 각 요소의 개수를 count해서 딕셔너리로 저장해준다.
import collections


def solution1(participant, completion):
    # !카운터 끼리는 빼기 가능하다.
    # - 동일한 키에 대해서 값을 빼준 결과를 리턴한다.
    answer = collections.Counter(participant) - collections.Counter(completion)
    # print(answer)
    return list(answer.keys())[0]


# - 내 정답
def solution(participant, completion):
    data = dict()

    for c in completion:
        if data.get(c) == None:
            data[c] = 1
        else:
            data[c] += 1

    for p in participant:
        if data.get(p) == None:
            return p
        data[p] -= 1
        if data[p] == 0:
            data.pop(p)


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution1(participant, completion))
