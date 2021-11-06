# https://programmers.co.kr/learn/courses/30/lessons/86971
# [Level2]
# * 정답 (40분)

# [다른 사람 풀이]
# - Union Find로 풀면 굉장히 빠르다는 것 같다. 근데 내가 실전에서 이 방법을 못 떠올릴 듯?
# - 다들 보통 BFS로 푼듯.. 음..

# [내 풀이]
# - 어렵지는 않았는 데 조금 헤맸다. DFS로 구현하다가 안되서 BFS로 변경함.
# * 처음에 DFS로 풀었는데 그렇게 안되는 문제였음 (함수 콜스택 초과됨)
# - 사실 처음부터 BFS로 풀면 될것 같다는 느낌 받았는데 그냥 재귀로 쉽게 가고 싶어서 그렇게 했다가 괜히 시간 날림 ㅎㅎ

# - 문제에서 "트리"라는 부분이 상당히 중요한 힌트임 (트리는 사이클이 없으니까.)

# [문제]
# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되있음 (사이클이 없음!)
# 이 전선들중 "하나"를 끊어서
# 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추기

# 송전탑의 개수 n, 그리고 전선 정보 wires
# 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때,
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return
from collections import deque

DISCONNECT = -1


# ! dfs(재귀)로 구현시 함수 콜스택 초과하므로 주의

# [BFS 메서드 정의]
def bfs(graph, start, visited):
    queue = deque([start])
    # *현재 노드를 방문 처리 (처음 1개만)
    visited[start] = True

    # 현재 노드와 연결된 다른 노드들 재귀적으로 방문
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def init_tree(n, wires):
    tree = [[] for _ in range(n+1)]

    # 편의를 위해 양방향 간선으로 표시
    for start, end in wires:
        tree[start].append(end)
        tree[end].append(start)
    # print(tree)
    return tree

# (함수 명을 왜 이렇게 대충 지었지??? 제출 전에 확인 좀 해! )


def get_abs(n, visited):
    tree1 = visited.count(True)
    tree2 = n - tree1
    return abs(tree1 - tree2)


def solution(n, wires):

    tree = init_tree(n, wires)
    answer = 999999
    for w in wires:
        # 방문 초기화
        visited = [False] * (n+1)
        # 전선 w[1]로 가는 경로는 단절 처리 한후 w[0]에서 bfs 시작
        visited[w[1]] = DISCONNECT
        bfs(tree, w[0], visited)
        # 방문 정보를 토대로 정답 도출
        answer = min(answer, get_abs(n, visited))
    return answer
