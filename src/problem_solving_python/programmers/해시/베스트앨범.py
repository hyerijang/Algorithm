
# * 정답 (40분)
# [Level 3]
# 그냥 무난했음, 난이도에 비하면 쉬웠다.

# [내코드]
from collections import defaultdict


def solution(genres, plays):

    # 1. 재생수 총합 기준으로  장르를 내림차순 정렬
    # 2. 장르 내에서
    #       - 가장 많이 재생 된 노래 먼저 수록 (내림차순)
    #       _ 재생 횟수 같으면 고유 번호 낮은 노래 먼저 수록

    # 장르별 재생수
    genre_plays = defaultdict(int)
    for i in range(len(genres)):
        name = genres[i]
        genre_plays[name] += plays[i]

    # info : 정렬을 위한 테이블
    # 장르총재생수, 곡의재생수, -(곡idx)
    # 오름차순 정렬한다.
    info = [(genre_plays[genres[idx]], plays[idx], -idx)
            for idx in range(len(plays))]
    info.sort(reverse=True)
    print(info)

    # 장르별 선정된 곡 수
    selected_num_in_genres = {genre: 0 for genre in genre_plays.keys()}
    answer = []
    for song in info:
        idx = -(song[-1])
        g = genres[idx]
        if selected_num_in_genres[g] < 2:  # 장르별 최대 2곡 선정 가능
            selected_num_in_genres[g] += 1
            answer.append(idx)

    return answer
