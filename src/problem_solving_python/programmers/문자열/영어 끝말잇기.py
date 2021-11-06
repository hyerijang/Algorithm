# https://programmers.co.kr/learn/courses/30/lessons/12981
# [Level 2]
# * 정답 (17분)
# - 무난히 쉬웠음.

def solution(n, words):
    answer = [0, 0]

    data = dict()

    # 이전 글자의 마지막 문자
    # 초기화 : 첫글자의 첫단어
    last = words[0][0]

    for idx, word in enumerate(words):
        # 이미 등장했던 단어이면 종료
        if data.get(word) != None:
            # print(f"{word}는 {data[word]}번에 등장한 적 있는 단어이고 탈락자는 {idx%n +1}, {idx //n +1}")
            answer = [idx % n + 1, idx // n + 1]
            break
        # 틀린 단어를 말한 경우
        if last != word[0]:
            # print(f"{word}는 {last}로 시작하는 단어가 아니고 탈락자는 {idx%n +1}, {idx //n +1}")
            answer = [idx % n + 1, idx // n + 1]
            break

        data[word] = idx
        last = word[-1]

    return answer
