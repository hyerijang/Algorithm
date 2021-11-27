# https://leetcode.com/problems/valid-palindrome/
# 파이썬 알고리즘 인터뷰 p.138

# [내 답안] 211127
class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = []

        # 정규식으로 필터링 했으면 더 빠르고 좋았을 듯.
        for c in s:
            if c.isalnum():
                data.append(c.lower())

        # 인덱스를 써서 비교했음. 나쁘지는 않은데,
        # if s == s[::-1] 처럼 슬라이싱으로 뒤집어서 비교하는 게 더 간결하게 표현됬을듯. 시간은 2배 더 걸렸겠지만...
        for idx in range(len(data)):
            if data[idx] != data[-idx-1]:
                return False

        return True
