import heapq
# 파이썬에서 기본적으로 제공하는 힙은 최소힙이다.


def minHeapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


def maxHeapsort(iterable):
    # [최대힙] : 최소 힙을 응용하여
    # !데이터의 부호를 바꾸어서 넣고 뺀다.
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)  # 부호 주의

    for i in range(len(h)):
        result.append(-heapq.heappop(h))  # 부호 주의
    return result


result = minHeapsort([1, 3, 5, 7, 9, 2, 4, 8, 6, 0])
print(result)

result = maxHeapsort([1, 3, 5, 7, 9, 2, 4, 8, 6, 0])
print(result)
