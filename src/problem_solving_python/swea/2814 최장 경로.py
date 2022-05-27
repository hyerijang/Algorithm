# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 2814. 최장 경로

# N개의 정점과 M개의 간선, 가중치가 없는 무방향 그래프에서의
# 최장 경로의 길이를 계산
from collections import defaultdict

t = int(input())

for case in range(t):
    # N개의 정점과 M개의 간선
    n, m = map(int, input().split())

    graph = defaultdict(set)

    for _ in range(m):
        x, y = map(int, input().split())
        #  두 정점 사이에 여러 간선이 존재할 수 있지만, 사실 재방문할수 없으므로 중복은 제거한다.

        graph[x].add(y)
        graph[y].add(x)

    answer = 0
    visited = [False for _ in range(n + 1)]
    visited[0] = True


    def dfs(start: int, length: int):
        global answer
        if answer < length:
            answer = length

        if length == n:  # 종료조건 : 모든 노드 방문
            return

        for next in graph[start]:
            if not visited[next]:
                visited[next] = True
                dfs(next, length + 1)
                visited[next] = False


    for start in range(1, n + 1):
        visited[start] = True
        dfs(start, 1)
        visited[start] = False

    print(f"#{case + 1} {answer}")
