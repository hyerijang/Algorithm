
# * 정답 (40분)
# - 음.. 너무 오래걸렸는데?

# 파티션(x)을 둘수 없는 거리 상대좌표
manhaton_no_x = [(0, 1), (1, 0)]

# 파티션(x)을 둘 수 있는 거리 상대좌표
manhaton_with_x = [(0, 2), (1, 1), (2, 0), (-1, 1), (1, -1)]

# 해당 상대 좌표에 모두 파티션이 있어야 거리두기 준수 한 것임
patition = {(0, 2): [(0, 1)],
            (1, 1): [(0, 1), (1, 0)],
            (2, 0): [(1, 0)],
            (-1, 1): [(-1, 0), (0, 1)],
            (1, -1): [(1, 0), (0, -1)]}


def outOfBound(x):
    return x not in range(5)


def isOK(room):

    result = True
    room = [list(r) for r in room]
    people = []

    for x in range(len(room)):
        for y in range(len(room)):
            # 사람 있는 곳이면 그 주변 검사
            if room[x][y] == 'P':

                # 파티션을 둘 수 없는 거리 검사
                for dx, dy in manhaton_no_x:
                    check_x, check_y = x+dx, y+dy
                    if outOfBound(check_x) or outOfBound(check_y):
                        continue
                    if room[check_x][check_y] == 'P':
                        # print(f"({x}, {y}) ({check_x}, {check_y}) 거리두기 불가")
                        result = False

                # 파티션을 놓을 수 있는 거리 검사
                for dx, dy in manhaton_with_x:
                    check_x, check_y = x+dx, y+dy

                    if outOfBound(check_x) or outOfBound(check_y):
                        continue

                    # 사람이 발견되면
                    if room[check_x][check_y] == 'P':
                        # 거리두기를 위해 파티션이 놓여있는지 확인
                        for l in patition[(dx, dy)]:
                            s_x, s_y = x+l[0], y+l[1]

                            if outOfBound(s_x) and outOfBound(s_y):
                                continue

                            if room[s_x][s_y] != 'X':
                                # print(f"({x}, {y}) ({check_x}, {check_y}) 파티션 없음")
                                result = False
                                break

    return result


def solution(places):
    answer = []
    for room in places:
        answer.append(int(isOK(room)))
    return answer
