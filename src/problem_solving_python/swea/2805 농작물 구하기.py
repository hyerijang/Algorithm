# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 2805. 농작물 수확하기 D3


t = int(input())

for case in range(t):
    answer = 0

    # 입력
    n = int(input())  # 농장의 크기 (항상 홀수)
    crop_values = [list(map(int, list(input()))) for _ in range(n)]

    # 수확 : 마름모 범위
    center = n // 2

    # 각 행에서 수확해야할 농작물 개수
    rhombus = list(range(1, n, 2)) + list(range(n, 0, -2))

    for y, num in enumerate(rhombus):
        answer += sum(crop_values[y][center - num // 2: center + num // 2 + 1])

    print(f"#{case + 1} {answer}")
