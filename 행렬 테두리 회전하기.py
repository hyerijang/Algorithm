def init(rows, columns):
    li = [[0] * (columns+2) for _ in range(rows + 2)]  # 테투리를 0으로 둘러쌈

    n = 1
    for y in range(1, rows+1):
        for x in range(1, columns+1):
            li[y][x] = n
            n += 1

    # print(li)
    return li


def rotation(li, x1, y1, x2, y2):
    nums = []
    dest = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d = 0

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if x not in [x1, x2] and y not in [y1, y2]:  # 안쪽인 경우
                continue
            else:
                nums.append(li[x][y])

                if x in (x1, x2) and y in (y1, y2):  # 꼭지점인 경우
                    print(li[x][y], '꼭짓점')
                    d += 1  # 방향 전환
                    if d == 4:
                        return min(nums)

    print(nums)
    # print("돌려야하는 숫자 개수 : ", (x2-x1+y2-y1) * 2)

    return min(nums)


def solution(rows, columns, queries):
    li = init(rows, columns)

    for q in queries:
        x1, y1, x2, y2 = q
        print(x1, y1, x2, y2)
        # print(li[x1][y1], li[x2][y2])
        rotation(li, x1, y1, x2, y2)
    answer = []
    return answer


my = solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])

if my != [8, 10, 25]:
    print('틀림', my, [8, 10, 25])
