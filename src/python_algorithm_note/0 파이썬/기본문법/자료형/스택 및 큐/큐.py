# 중요
# deque 라이브러리 활용!!!!!
from collections import deque

# list로 구현? 기능적으로는 큐 구현인데 시간 복잡도가 큐 아님


# 큐 연산
# 삽입 : append(i)
# 삭제 : popleft() <-- stack과 차이점

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
print(queue)

queue.popleft()  # ! popleft() 임에 주의
print(queue)

queue.append(1)
queue.append("latest")


print(queue)  # 먼저 들어온 순으로 출력
queue.reverse()  # 큐를 역순으로 변경
print(queue)  # 가장 마지막에 들어온 애부터 출력

# print(stack[::-1])  # 가장 마지막에 들어온 애부터 출력
