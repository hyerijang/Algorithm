
# ! 틀림 (40분)
# -  BFS로 풀려고했는데.. 보통 DFS 로 푸나봐

# [모범답안]
# * 좀 직관적으로 이해하기 어려운 코드긴 하네.
# - 딕셔너리를 사용하여 그래프를 만든 후에, 그래프를 시작에서부터 하나씩 pop(0) 시켜주고, pop(0)을 다시 재귀로 넣는다.
import collections
answer = []
graph = collections.defaultdict(list)


def dfs(s):
    while graph[s]:
        dfs(graph[s].pop(0))

    if not graph[s]:  # 모든 노드를 방문 했으면
        answer.append(s)  # 해당 노드를 경로에 추가함
        return


def solution(tickets):

    for a, b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort()

    dfs("ICN")

    return answer[::-1]  # 역으로 리턴
