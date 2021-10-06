
# ! 틀림 (30분)
# BFS란거 알고 있으면서 왜 큐를 안썼지??

# ! 틀림 (50분)
# 알고있다고 풀수 있는건 아니네... 다시 풀어봐야할 듯

# [모범답안]
# - BFS 풀이
# - zip 사용해서 단어의 각 글자 비교
# - visit 대신  dict에 시작지점부터의 거리 저장!

from collections import deque


# current 와 연결되어있는 단어들을 리턴한다.
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    # *BFS 사용
    # 방문한적 있는 단어의 거리 저장하는 dict  // visit 대신 사용함
    dist = {begin: 0}  # ! 방문 표시
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            # print(next_word, end=' ')
            if next_word not in dist:
                dist[next_word] = dist[current] + 1  # ! 방문 표시
                queue.append(next_word)
        # print()

    return dist.get(target, 0)


solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"])
