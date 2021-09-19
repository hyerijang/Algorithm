n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


print(graph)


# 입력 값 예시
# 5
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 1 0 1
# 1 1 1 1 1
