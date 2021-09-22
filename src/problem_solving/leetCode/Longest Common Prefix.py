# https://leetcode.com/problems/longest-common-prefix/
# 모범답안
def longestCommonPrefix1(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs, key=len)  # 가장 짧은 단어 찾기
    for i, ch in enumerate(shortest):  # 가장 짧은 단어에 대하여 다른 글자들을 한글자씩 비교
        for other in strs:
            if other[i] != ch:  # 다른 부분 발견시
                return shortest[:i]  # slice 하여 유효한 prepix만 리턴
    return shortest


def longestCommonPrefix(strs) -> str:
    result = ''
    min_len = 987654321
    for s in strs:
        min_len = min(len(s), min_len)

    i = 0
    while i < min_len:
        cur = strs[0][i]
        for s in strs:
            if cur != s[i]:
                return result
        result += cur
        i += 1

    return result


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
