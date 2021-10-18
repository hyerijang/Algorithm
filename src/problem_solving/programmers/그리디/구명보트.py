# https://programmers.co.kr/learn/courses/30/lessons/42885
# [Level 2]
# *정답(20분) : 설계 10, 코딩 10
# -쉽네. 투포인터라서 공간복잡도도 안높을듯. 오랜만에 맘에드는 풀이임@@

def solution(people, limit):
    people.sort()

    count = 0

    # 투포인터 방식
    # left: 남은 인원 중 가장 무거운 사람의 인덱스
    # right: 남은 인원 중 가장 가벼운 사람의 인덱스
    left, right = 0, len(people) - 1

    while left <= right:
        # 한명만 남은 경우 바로 탈출시키고 끝
        if left == right:
            count += 1
            break

        # 무게 제한 >= left, right이면 둘 다 태움
        if limit >= people[left] + people[right]:
            left += 1
            right -= 1
            count += 1
        # 아니면 무거운 쪽만 태워보냄
        else:
            right -= 1
            count += 1

    return count
