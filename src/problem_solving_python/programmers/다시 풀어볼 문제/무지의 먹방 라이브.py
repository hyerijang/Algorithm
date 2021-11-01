# https://programmers.co.kr/learn/courses/30/lessons/42891
# 우선순위 큐를 사용하여 구현한 예시
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []  # 우선순위 큐
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0  # 먹기위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 전체 food  개수

    while sum_value + ((q[0][0] - previous) * length) <= k:  # k는 현재 남은 시각
        now = heapq.heappop(q)[0]  # 시간이 가장 적게 걸리는 음식을 먹는데 시간
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

# 내 풀이 - 효율성 테스트 시간 초과
# def solution(food_times, k):
#     answer = 0
#     time = 0
#     while time <= k:
#         is_no_food = True
#         for i in range(len(food_times)):
#             if food_times[i] == 0:  # 다 먹은 음식인 경우
#                 continue
#             if time == k:
#                 # print('정답', i+1)
#                 return i+1
#             else:
#                 food_times[i] -= 1  # 먹음
#                 time += 1
#                 # print(time, '초에 먹음', i+1)
#                 is_no_food = False
#         if is_no_food:
#             return -1

#     return answer


print(solution([3, 1, 2], 5))
