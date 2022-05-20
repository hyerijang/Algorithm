# https://www.acmicpc.net/problem/23288
# ! 틀림 , 문제 잘못 이해함 (1시간 30분)

from copy import deepcopy
import sys
sys.stdin = open("input.txt", "r")

동 = (0, 1)
서 = (0, -1)
남 = (1, 0)
북 = (-1, 0)


한글 = {동: "동", 서: "서", 남: "남", 북: "북"}
아랫면 = 5


def 입력():
    n, m, k = map(int, input().split())

    지도 = []
    for i in range(n+1):
        if i == 0:
            지도.append([0 for _ in range(m+1)])
        else:

            지도.append([0]+list(map(int, input().split())))

    return n, m, k, 지도


def 주사위굴림(주사위: list, 방향: tuple):

    if 방향 == 북:
        주사위[0], 주사위[2], 주사위[4], 주사위[5] = 주사위[2], 주사위[4], 주사위[5], 주사위[0]
    elif 방향 == 남:
        주사위[0], 주사위[2], 주사위[4], 주사위[5] = 주사위[5], 주사위[0], 주사위[2], 주사위[4]
    elif 방향 == 동:
        주사위[1], 주사위[2], 주사위[3], 주사위[5] = 주사위[5], 주사위[1], 주사위[2], 주사위[3]

    elif 방향 == 서:
        주사위[1], 주사위[2], 주사위[3], 주사위[5] = 주사위[2], 주사위[3], 주사위[5], 주사위[1]
    else:
        print("잘못된방향입력")

    return 주사위


반대방향 = {동: 서, 서: 동, 남: 북, 북: 남}
시계방향 = {동: 남,
        남: 서,
        서: 북,
        북: 동}
anti = {동: 북,
        북: 서,
        서: 남,
        남: 동}


def 범위내(x, y, n, m):
    if 1 <= x <= n and 1 <= y <= m:
        return True
    return False


def 연속이동(x, y, n, m):
    c = 0
    for 이동방향 in [동, 서, 남, 북]:
        nx, ny = x + 이동방향[0], y + 이동방향[1]  # 갱신

        if 범위내(nx, ny, n, m):
            c += 1
            x, y, = nx, ny
        else:
            break

    return c


def simulation():
    # (0) 초기설정
    주사위 = [2, 4, 1, 3, 5, 6]
    n, m, k, 지도 = 입력()

    이동방향 = 동
    dice_x, dice_y = 1, 1

    # [주사위의 이동]
    score = 0
    print("0", 한글[이동방향])
    for time in range(1, k+1):
        # (1) 주사위가 이동 방향으로 한 칸 굴러간다.
        x, y = dice_x + 이동방향[0], dice_y + 이동방향[1]

        if not 범위내(x, y, n, m):
            # - 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
            반대 = deepcopy(반대방향[이동방향], B)
            x, y = dice_x + 반대[0], dice_y + 반대[1]

        dice_x, dice_y = x, y  # 갱신

        주사위굴림(주사위, 이동방향)
        # (2) 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
        # - 점수획득
        B = 지도[dice_x][dice_y]
        C = 연속이동(dice_x, dice_y, n, m)
        score += C * B

        # (3) 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
        A = 주사위[아랫면]
        B = 지도[dice_x][dice_y]
        if A > B:
            # (3.1) A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
            바뀐방향 = deepcopy(시계방향[이동방향])
            print(time, x, y, 한글[이동방향], 한글[바뀐방향], "시계")
            이동방향 = 바뀐방향
        elif A < B:
            # (3.2)A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
            바뀐방향 = deepcopy(anti[이동방향])
            print(time, x, y, 한글[이동방향], 한글[바뀐방향], "반시계")
            이동방향 = 바뀐방향
        else:
            # (3.3)A = B인 경우 이동 방향에 변화는 없다.
            print(time, x, y, 한글[이동방향], 한글[바뀐방향])

    return score


print(simulation())
