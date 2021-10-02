#
# [카운터]
# - dict의 하위 객체
# - Counter()의 시간복잡도 =>O(N)

# [카운터끼리 빼기]
# - 프로그래머스, 완주하지 못한 선수
# - collections의 Counter를 사용하면 리스트내 각 요소의 개수를 count해서 딕셔너리로 저장해준다.
import collections

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution1(participant, completion):
    # !카운터 끼리는 빼기 가능하다!
    # - 동일한 키에 대해서 값을 빼준 결과를 리턴한다.
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]


print(solution1(participant, completion))
