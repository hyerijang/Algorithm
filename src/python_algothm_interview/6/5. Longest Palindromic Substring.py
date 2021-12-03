# https://leetcode.com/problems/longest-palindromic-substring/

# 가장 긴 팰린드롬 서브스트링을 리턴하기

# [Constraints]
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


def longestPalindrome(s: str) -> str:

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s)-1):
        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)

    print(f"result = {result}")
    return result


longestPalindrome("babad")
longestPalindrome("cbbd")
longestPalindrome("a")
longestPalindrome("ac")


def mylongestPalindrome(s: str) -> str:
    result = s
    length = -1

    for idx in range(len(s)):
        start = idx
        end = idx
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start = start - 1
                end = end + 1
            else:
                break

        if length < end - start:
            length = end - start
            result = s[start:end]
            print(length, s[start:end])

    print(result)
    return result
