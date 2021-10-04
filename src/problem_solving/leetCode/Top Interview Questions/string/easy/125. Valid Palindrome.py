#
#  * 정답 (7분)

# [모범답안]
# https://leetcode.com/problems/valid-palindrome/discuss/770465/Python-Two-pointers-O(n)-time-and-O(1)-space-explained
# * Two Pointer 방식으로 구현하면
# - O(N) 시간으로 더 빠르게 탐색하면서 공간복잡도를 O(1)으로 할 수 있다.
# - 근데 코드가 더 복잡해지긴 할듯

# [내 답안]
# - 시간복잡도는 아마 O(N) //하위 5.66%
# - 공간복잡도도 아마 O(N) //하위 7.24%


def isPalindrome(s: str) -> bool:
    text = []
    for c in s:
        if c.isalnum():
            text.append(c.lower())

    return text == text[::-1]


print(isPalindrome("0P"))
