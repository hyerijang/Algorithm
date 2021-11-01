# https://programmers.co.kr/learn/courses/30/lessons/42577
# [Level 2]
# * 정답 (20분)
# * 접두사 비교시 startswith으로 비교했으면 더 간단했을 것임

import collections


def solution(phone_book):
    # 공백제거
    for phone_number in phone_book:
        phone_number.replace(" ", "")

    # * 역순 정렬
    # - 긴 것을 검사했을 때 접두사 발견할 확률 높으므로
    phone_book.sort(reverse=True)

    # 딕셔너리로 만들기 귀찮아서 쓴건데 시간복잡도는 잘 모르겠네 #- O(N)이라고 한다!
    data = collections.Counter(phone_book)
    # * 접두사 비교
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if data.get(phone_number[0:i]) != None:
                return False  # 접두어가 있음

    return True  # 접두어가 없음


phone_book = ["12", "123", "1235", "567", "88"]
print(solution(phone_book))
