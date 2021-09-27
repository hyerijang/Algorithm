# https://programmers.co.kr/learn/courses/30/lessons/60057
# 실패. 아래 코드는 다른 사람 코드임

def solution(s):
    # print(s)
    answer = len(s)
    data = dict()
    for size in reversed(range(1, (len(s)+1)//2 + 1)):
        for start in range(0, len(s), size):
            tmp = s[start:start+size]

            if tmp == '':
                continue

            repeatCount = (len(s) + 1) // size
            # print('후보', tmp, repeatCount)
            for count in range(2, repeatCount):
                print(count)
                if tmp * count in s:
                    data[tmp] = count
                    # print(' -> 중복있음', tmp * count)
                    answer = answer - size * (count-1) + 1
                    break

    return answer


solution('aabbaccc')
