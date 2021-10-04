
# ! 틀림 (10분)

# [모범답안]
# - use Two Pointer, go from the star and end of the String, swap pair of element
def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]

# * 그 외 정답
# s = s.reverse()

# [틀린 풀이]
# * s = s.reverse()은 되고
# ! s[::-1은 안됨]


def reverseString(s):
    # - 해당 방식으로는 call by refernce가 안먹히나봄
    # - (추측) s[::-1]로 하면 s와는 별개의 아예 새로운 공간을 할당 받아서 이를 저장하기 때문에 그런듯
    s = s[::-1]
    print(s)


s = ["h", "e", "l", "l", "o"]
reverseString(s)
print(s)
