# https://programmers.co.kr/learn/courses/30/lessons/42587
# [Level 2]
# *정답(30분) , 좀 오래걸렸네

from collections import deque
import collections

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.


def priority_counter(queue):
    data = dict()
    for q in queue:
        priority = q[0]
        if data.get(priority) is not None:
            data[priority] += 1
        else:
            data[priority] = 1
    return data


def solution(priorities, location):
    answer = 0

    # 큐 사용
    queue = deque()

    name = 0
    for priority in priorities:
        queue.append((priority, name))
        name += 1

    # 우선순위 별 개수 카운트
    count = priority_counter(queue)

    while queue:
        document = queue.popleft()
        document_p = document[0]
        # print(queue)

        priority_list = list(count.keys())
        priority_list.sort(reverse=True)
        # 우선순위 더 높은 문서가 큐에 남아있으면
        if priority_list[0] > document_p:
            queue.append(document)  # 다시 넣기
        # 현재 문서가 가장 우선순위 높은 문서인 경우
        else:
            # 출력
            answer += 1
            count[document_p] -= 1
            if count[document_p] == 0:  # 큐 내에 해당 우선순위인 문서가 0개이면
                count.pop(document_p)  # 딕셔너리에서 그 우선순위 삭제
            if document[1] == location:
                return answer

    return answer


solution([2, 1, 3, 2], 2)
