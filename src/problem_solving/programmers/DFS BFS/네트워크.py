
# * 정답 (15분)
# - 뭔가 표준 라이브러리로 신기하게 푸는 방법이 있었던거 같은데?? 내 착각인가보다
# ! 아 서로소 집합 자료구조였다. (10. 그래프 이론)
# ! 근데 서로소 집합으로.. 풀수 있긴 한데 그걸 구현하느니 BFS 푸는게 나을 듯. 훨씬 쉬움!
# - 그냥 딱 정석적인 bfs로 푸는 문제!

def bfs(computer, start, visit):
    if start in visit:
        return False

    visit.append(start)

    for node in range(len(computer[start])):
        if computer[start][node] == 1:
            bfs(computer, node, visit)

    return True


def solution(n, computers):
    answer = 0
    visit = []

    for i in range(n):
        answer += bfs(computers, i, visit)

    print(answer)
    return answer


computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

solution(3, computers)
