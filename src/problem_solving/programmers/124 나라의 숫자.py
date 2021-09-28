# https://programmers.co.kr/learn/courses/30/lessons/12899
# 정답
def solution(n):
    result = ''

    while True:
        n -= 1
        if n % 3 == 0:
            result += '1'  # 1
        elif n % 3 == 1:
            result += '2'  # 2
        else:
            result += '4'  # 4

        n = n//3

        if n <= 0:
            break
    return result[::-1]


i = 4
print(i, solution(i))

for i in range(1, 9):
    print(i, solution(i))
