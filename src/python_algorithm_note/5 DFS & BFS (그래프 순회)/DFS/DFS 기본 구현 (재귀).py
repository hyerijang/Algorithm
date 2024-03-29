def dfs(graph, v, visit):
    # *현재 노드를 방문 처리
    visited[v] = True  # 방문 처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드들 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)  # 재귀


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


dfs(graph, 1, visited)
