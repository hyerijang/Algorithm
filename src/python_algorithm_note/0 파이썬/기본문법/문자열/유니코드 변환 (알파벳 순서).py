
# ! ord()
# - 문자의 유니코드 값을 돌려주는 함수이다.

# ! chr()
# - 숫자에 해당하는 유니코드 문자를 돌려준다.
print(ord('A'), chr(65))


def titleToNumber(columnTitle: str) -> int:
    answer = 0

    for c in columnTitle:
        answer = answer * 26 + ord(c) - ord('A') + 1

    print(answer)
    return answer


titleToNumber("A")
