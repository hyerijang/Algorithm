# https://programmers.co.kr/learn/courses/30/lessons/42883
# ! 틀림 (1시간)
# - 10번 테스트케이스에 초과 뜨네...

def solution(number, k):

    while k:  # k번 만큼 반복
        k -= 1
        removed = False

        # i 번째 글자가 i+1번재 글자보다 작은경우 i번째 글자를 뺀다.
        for i in range(len(number) - 1):
            if number[i] < number[i+1]:
                number = number[0:i] + number[i+1:]
                removed = True
                break

        if not removed:
            number = number[:-1]

    return number
