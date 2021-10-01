# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# * 정답 (40분)
# - 맞긴 했는데 오래걸렸고, 썩 깔끔하지 않은 코드임
# ! 여기 주의 할 것

# [ 좋은 예시 : https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3
def solution(new_id):
    # 1단계 모두 소문자로 변환
    new_id = new_id.lower()

    # 2단계
    new_id = list(new_id)
    i = 0
    size = len(new_id)
    while i < size:
        c = str(new_id[i])
        if c.isdecimal() or c.islower():  # 숫자 혹은 소문자인경우
            i += 1
            continue
        elif c in ['-', '_', '.']:
            i += 1
            continue
        # 허용문자가 아닌경우 뺀다
        new_id.pop(i)
        size -= 1

    # 3단계
    new_id = "".join(new_id)
    i = new_id.find('..')
    while i >= 0:  # '.'이 중첩되어 있는 부분 찾음
        i += 1  # 두번째 '.'부터 삭제 시작

        while i < len(new_id) and new_id[i] == '.':  # 연속되는 . 모두 제거
            # print(new_id)
            new_id = new_id[:i]+new_id[i+1:]
            # print(new_id)
        i = new_id.find('..')

    # 4단계
    while new_id.startswith('.'):
        new_id = new_id[1:]

    while new_id.endswith('.'):
        new_id = new_id[:-1]
    # print(new_id)

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    new_id = new_id[:15]
    # print(new_id)
    while new_id.endswith('.'):
        new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


# print(solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi")
# print(solution("=.=") == "aaa")
# print(solution("z-+.^.") == "z--")
print(solution("abcdefghijklmn.p") == "abcdefghijklmn")
