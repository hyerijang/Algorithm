# https://leetcode.com/problems/plus-one/submissions/
# *정답 (18분)
# - 릿코드 오랜만에 푸니까 좀 헤맸음. 그거 빼곤 뭐

# [모범답안]
# https://leetcode.com/problems/plus-one/discuss/24085/Simple-Python-solution-with-explanation-(Plus-One)
# - 리스트 컴프리헨션 멋잇당
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]


# [내 답안]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # number를 문자로 변환
        number = ""
        for d in digits:
            number += str(d)

        # number를 숫자로 변환후 +1
        number = int(number)
        number += 1

        digits = []
        while number:
            digits.append(number % 10)
            number = number//10
        digits.reverse()

        return digits
