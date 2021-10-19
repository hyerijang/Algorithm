# [Level 2]
# *정답(45분) : 설계 10, 코딩 40
# - re 정규식 때무에 좀 해맴.
# - 나머지는 쉬웠음... 좀 더 빨리 구현할 수도 있었을텐데 아쉽다.


import re
from collections import defaultdict
HEAD = 0
NUMBER = 1


def solution(files):
    # pattern는 파일명의 HEAD, NUMBER
    # 해당 패턴을 갖는 파일들의 인덱스를 dict로 관리
    pattern_index = defaultdict(list)

    pattern_list = []

    for idx in range(len(files)):
        data = re.split("(\d+)", files[idx])
        # HEAD 부분은 영어 소문자로 변환
        data[HEAD] = data[HEAD].lower()
        # NUMBER 부분은 문자열이 아닌 숫자로 저장
        data[NUMBER] = int(data[NUMBER])
        # pattern는 파일명의 HEAD, NUMBER만 포함
        pattern = data[0:2]
        # 해당 HEAD, NUMBER의 등장 횟수 카운트
        pattern_index[str(pattern)].append(idx)
        pattern_list.append(pattern)

    # 정렬: HEAD를 기준으로 사전순 정렬 후 HEAD가 동일하면 Number 순으로 정렬
    pattern_list.sort()
    print(pattern_list)

    answer = []

    # 출력:
    for f in pattern_list:
        pattern = str(f)

        # 이전에 출력된 패턴인 경우 pass
        if len(pattern_index[pattern]) == 0:
            continue
        else:
            # 해당 패턴을 지닌 모든 파일명 answer에 포함
            for idx in pattern_index[pattern]:
                answer.append(files[idx])
            # 전부 조회 후 비움
            pattern_index[pattern].clear()

    return answer
