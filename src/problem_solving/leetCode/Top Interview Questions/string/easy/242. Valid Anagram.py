
# * 정답 (2분)
# - 카운터 쓰니까 매우 쉽군

import collections


def isAnagram(s: str, t: str) -> bool:

    s_counter = collections.Counter(s)
    t_counter = collections.Counter(t)

    if s_counter == t_counter:
        return True

    return False
