
# ! 실패 (10분)
# * 분명 풀어본 문제인데... 틀렸네
# - 아이디어는 떠올렸는데 이게 맞나 ? 하기도 했고
# - 결국 구현을 못해서 틀림 ㅎㅎ ㅠ


# [모범답안]
# https://leetcode.com/problems/longest-palindromic-substring/solution/
# *Time complexity : O(n^2)
# *Space complexity : O(1)
# - solution이 자바 코드라 그거 참고해서 내가 파이썬으로 바꿈

def expandAroundCenter(s: str, left: int, right: int) -> int:  # 길이 리턴
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def longestPalindrome(s: str) -> str:
    answer = ""

    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i+1)
        candidate = s[i:i + max(len1, len2)]
        # 후보의 길이가 더 길면
        if len(candidate) > len(answer):
            answer = candidate  # 교체
    print("정답:", answer)
    return answer


longestPalindrome("babad")
