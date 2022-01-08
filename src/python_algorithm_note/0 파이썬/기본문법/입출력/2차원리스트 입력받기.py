n = int(input())


# 방법 1
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


print(graph)


# 방법 2 : 리스트 컴프리 헨션사용해서 1줄로 표현
graph = [list(map(int, input().split())) for _ in range(n)]

# 입력 값 예시
# 5
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 1 0 1
# 1 1 1 1 1
