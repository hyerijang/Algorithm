# DFS BFS 모두 가능
# 하지만 상하좌우 방문 시, DFS로 재귀 호출하는게 좀 더 깔끔하니까 DFS
# 음료수 얼려 먹기
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # cf. str은 iterable


def dfs(x, y):
    # 범위 검사
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
