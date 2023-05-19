# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWHPkqBqAEsDFAUn&categoryId=AWHPkqBqAEsDFAUn&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 3752. 가능한 시험 점수 [다시 풀 것]
# 아이디어가 좀 필요한 문제네.. 그냥 BFS나 조합 쓰면 시간 초과되므로 주의.


# 입력
cases = int(input())
for case in range(1, cases+1):
    n = int(input())
    scores = list(map(int, input().split()))

    # 한 학생이 받을 수 있는 점수 : 최소 0점, 최대 sum(scores)점
    visited = [True] + [False] * sum(scores) # 0점은 반드시 존재
    possible = [0] # 학생들이 받을 수 있는 점수

    # 학생들이 받을 수 있는 점수를 계산
    for s_idx in range(len(scores)):
        # 문제를 1개씩 늘려가며 새로운 점수 계산해본다.
        for p_idx in range(len(possible)):
            new_score = scores[s_idx] + possible[p_idx]
            if not visited[new_score]:
                visited[new_score] = True
                possible.append(new_score)

    ans = 0
    for s_idx in possible:
        ans+=1
    print("#{} {}".format(case, ans))
