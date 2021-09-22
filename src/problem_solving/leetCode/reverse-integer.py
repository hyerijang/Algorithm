# https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    s = str(abs(x))
    s = s[::-1]

    result = 0

    if x < 0:
        result = - int(s)

    else:  # 양수 인경우
        result = int(s)

    if result < - pow(2, 31) or result > pow(2, 31) - 1:
        return 0

    return result


print(reverse(1534236469))
