
from collections import deque


# [BFS 메서드 정의]
def bfs(graph, start, visit):
    # !큐 구현
    # *현재 노드를 삽입하고
    queue = deque([start])
    # *현재 노드 방문 처리 (처음 1개만)
    visited[start] = True

    # 현재 노드와 연결된 다른 노드들 재귀적으로 방문
    while queue:
        v = queue.popleft()  # - 실질적으로 방문하는 시점
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)  # ! 큐에 넣는 조건 : 인근 노드일것 && 방문하지 않은 노드 일 것
                # * 큐에 넣은 후 방문했다고 표시

                # ==방문 표시 미리 함 ==
                # - (큐는 선입후출이므로 다음 반복문에서 똑같은 노드 방문하지 않기위해서는 미리 표시해둬야함)
                visited[i] = True


graph = [
    [],  # 일반적으로 그래프 문제에서 노드 1번부터 시작하므로 0번 노드는 비워준다.
    [2, 3, 8],  # 1번 인덱스로 시작(1번 노드와 연결된건 2,3,8번 노드이다)
    [1, 7],  # (2번 노드와 연결된건 1, 7번 노드이다)
    [1, 4, 5],  # 낮은 인덱스부터 방문하기로 했으므로 내부 요소는 오름차순이어야함
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]  # 8번 노드
]

# 노드 개수 + 1 (0번 노드 포함)
n = 9

# 방문 정보 기록
visited = [False] * n


bfs(graph, 1, visited)
