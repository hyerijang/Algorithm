
#  * 정답 (3분)
#  - 역시 내장함수가 빠르긴 빠르다.


def strStr(haystack: str, needle: str) -> int:

    answer = haystack.find(needle)
    return answer


print(strStr("aa", "z"))
