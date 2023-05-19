# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# [정답]

from collections import defaultdict

def dump(height_to_loc:dict):
    heights = height_to_loc.keys()
    # 최저점, 최고점 높이
    lh, hh = min(heights), max(heights)

    # 최고점 중 한곳에서 상자 하나 빼서
    hloc = height_to_loc[hh].pop()
    height_to_loc[hh-1].append(hloc)
    # 최저점인 곳 중 하나에 둔다.
    lloc = height_to_loc[lh].pop()
    height_to_loc[lh + 1].append(lloc)

    if not height_to_loc[hh] :
        del height_to_loc[hh]

    if not height_to_loc[lh]:
        del height_to_loc[lh]

    return

def solution():
    for idx in range(1,11):
        dump_count = int(input()) #가로길이
        boxes = list(map(int, input().split())) #각 위치에서 상자의 높이


        # key: height, value : 위치의 리스트
        height_to_loc = defaultdict(list)
        for loc in range(len(boxes)):
            h = boxes[loc]
            # if height_to_loc.get(h) == None:
            #     height_to_loc[h] = []
            height_to_loc[h].append(loc)

        while dump_count:
            dump(height_to_loc)
            dump_count-=1


        heights = height_to_loc.keys()
        # 최저점, 최고점 높이 차
        answer = max(heights) - min(heights)

        print("#{0} {1}".format(idx, answer))
        idx+=1

solution()