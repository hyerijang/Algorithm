# https://programmers.co.kr/learn/courses/30/lessons/42840
# * 정답 (30분 걸림)
# - 난이도에 비해 너무 오래걸렸다.


pattern = [[1, 2, 3, 4, 5],  # 1번 수포자
           [2, 1, 2, 3, 2, 4, 2, 5],  # 2번 수포자
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]  # 3번 수포자


def solution(answers):
    high_scorer = []

    count = [0, 0, 0]
    for i in range(len(answers)):
        for who in range(len(pattern)):
            if pattern[who][i % len(pattern[who])] == answers[i]:
                count[who] += 1

    # 고득점자 찾기
    highest_score = max(count)
    for i in range(len(count)):
        if count[i] == highest_score:
            high_scorer.append(i+1)

    return high_scorer


answer = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

solution(answer)
