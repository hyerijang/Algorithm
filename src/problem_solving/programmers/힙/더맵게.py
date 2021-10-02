# https://programmers.co.kr/learn/courses/30/lessons/42626
# * 정답 (30분)
# - 테스트 케이스 16번 못맞춰서 질문하기 보고 풀었음.
# - 16번 케이스 : print(solution([1, 2, 3], 6) == 2)


import heapq


def solution(scoville, K):
    answer = 0
    h = []  # heap으로 유지될 배열

    # 모든 원소를 차례대로 힙에 삽입
    for value in scoville:
        heapq.heappush(h, value)

    while len(h) > 1:
        print(h)
        first = heapq.heappop(h)
        if(first >= K):
            # print(first, "큼")
            return answer
        second = heapq.heappop(h)
        # print(first, second, h)
        answer += 1
        heapq.heappush(h, first + second * 2)

    # 마지막으로 만들어진 수가 스코빌 초과하는 경우
    if h[0] >= K:
        return answer

    # 만들 수 없는 경우
    return -1


print(solution([1, 2, 3], 6), 2)
