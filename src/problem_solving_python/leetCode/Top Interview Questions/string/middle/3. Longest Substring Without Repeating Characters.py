# Given a string s,
# ! 실패(20분)
# - substring을 어떻게 잘라서 비교해야할지 잘 모르겠음
# - 샘플 코드들도 봤는데 되게 어렵당.. 아래가 그나마 쉬운 코드임
#

# [모범답안]
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1005991/Python.-Cool-and-easy-solution.-O(n)-time.-O(1)-space.
# - 그림 그려가면서 풀어야할듯. 되게 어렵네
def lengthOfLongestSubstring(s: str) -> int:
    characters = set()
    left = right = ans = 0
    length = len(s)

    while right < length:
        if s[right] in characters:
            characters.remove(s[left])
            left += 1
        else:
            characters.add(s[right])
            right += 1
            ans = max(ans, right - left)

    return ans


# lengthOfLongestSubstring("bbbbb")
# lengthOfLongestSubstring("abcabc")
lengthOfLongestSubstring("pwwkew")
