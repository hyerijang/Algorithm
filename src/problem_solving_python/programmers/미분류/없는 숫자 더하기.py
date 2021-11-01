# 너무 쉬운데
def solution(numbers):
    answer = -1
    numbers.sort()

    sum = 0
    for n in numbers:
        sum += n

    answer = 45 - sum
    return answer
