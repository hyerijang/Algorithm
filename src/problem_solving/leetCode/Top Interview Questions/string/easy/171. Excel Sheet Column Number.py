
# *정답 (7분)
# - 유니코드 변환 함수 ord 생각 안나서 그건 찾아봄.

def titleToNumber(columnTitle: str) -> int:
    answer = 0

    for c in columnTitle:
        answer = answer * 26 + ord(c) - ord('A') + 1

    print(answer)
    return answer


titleToNumber("AA")
