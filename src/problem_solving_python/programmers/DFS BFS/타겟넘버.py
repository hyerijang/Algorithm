
# * 정답 (40분)
# - 오래걸렸당..

# [모범답안]
# -곱집합을 사용한 멋진 풀이!
from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# [내 풀이]


PLUS = 0
MINUS = 1


def dfs(i,  sum):
    # print(sum)
    if i == len(graph) - 1:
        if sum == t:
            return 1
        return 0

    count = dfs(i+1,  sum + graph[i+1][PLUS]) + \
        dfs(i+1, sum + graph[i+1][MINUS])

    return count


def solution(numbers, target):
    # 내림차순 정렬
    numbers.sort(reverse=True)

    global t
    t = target

    # 그래프 초기화
    global graph
    graph = [[n, -n] for n in numbers]

    answer = dfs(0, graph[0][PLUS]) + dfs(0, graph[0][MINUS])

    return answer


solution([1, 1, 1, 1, 1], 3)
