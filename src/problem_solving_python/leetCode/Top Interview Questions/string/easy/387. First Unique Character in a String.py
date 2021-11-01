
# * 정답 (13분)
# - 쉽긴한데 풀이가 좋다
# https://leetcode.com/problems/first-unique-character-in-a-string/solution/
# [모범답안]

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)  # ! Counter로 각 글자의 개수 셈

        # find the index
        for idx, ch in enumerate(s):  # ! enumerate로 문자열의 인덱스 생성
            if count[ch] == 1:
                return idx
        return -1


# [내풀이]
INF = 987654321


def firstUniqChar(s: str):
    data = dict()

    for i in range(len(s)):
        c = s[i]
        # 만난 적이 있는 문자이면
        if data.get(c) != None:
            data[c] = INF
        else:
            # 딕셔너리에 기록
            data[c] = i

    result = min(data.values())

    if result != INF:
        return min(data.values())

    return -1


firstUniqChar("leetcode")
