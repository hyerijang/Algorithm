
# * 정답 (12분)
# -쉬웠어

def solution(brown, yellow):

    total = brown + yellow

    # 세로길이(h)
    for h in range(1, total):
        if total % h != 0:
            continue

        # 가로길이(n)
        n = total // h

        # 현재 카펫의 brown, yellow 개수
        cur_b = n*h - (n - 2)*(h - 2)
        cur_y = (n - 2)*(h - 2)

        # 기억과 일치하면 리턴
        if cur_b == brown and cur_y == yellow:
            return [n, h]


solution(10, 2)
