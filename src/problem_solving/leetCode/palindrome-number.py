# https://leetcode.com/problems/palindrome-number/


def isPalindrome(x: int) -> bool:
    s = str(x)
    r = s[::-1]

    for i in range(len(s)):
        if s[i] != r[i]:
            return False

    return True


print(isPalindrome(1000021))
