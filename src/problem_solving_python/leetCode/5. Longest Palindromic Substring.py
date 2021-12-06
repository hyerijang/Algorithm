# https://leetcode.com/problems/longest-palindromic-substring/

# 가장 긴 팰린드롬 서브스트링을 리턴하기

# *정답
# - Runtime : 964 ms

# * 아래 예외처리 추가했으면 더 빠르게 동작 했을 것임 (244ms)
# 해당 사항이 없을 때 빠르게 리턴
# if len(s) < 2 or s == s[::-1]:
# return s

# [Constraints]
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(self, s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        answer = ''
        for i in range(len(s)):
            answer = max(answer, expand(self, s, i, i),
                         expand(self, s, i, i+1), key=len)

        return answer
