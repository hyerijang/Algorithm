
# https://programmers.co.kr/learn/courses/30/lessons/60059
# FIXME: 실패. 50분 가량 구현했는데 잘 모르겠음
# TODO: 이코테 518쪽에 예제 코드 나와있음. 코드 보면서 복습할 것

# def sumBumps(data):
#     total = 0
#     for line in data:
#         total += sum(line)
#     return total


# def rotated(a):
#     n = len(a)
#     m = len(a[0])

#     result = [[0] * n for _ in range(m)]

#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = a[i][j]

#     return result


# def ignEmpty(key):
#     for line in key:
#         if sum(line) == 0:
#             key.remove(line)

#     return key


# INF = 987654321


# def reverseZeroOne(a):
#     n = len(a)
#     m = len(a[0])

#     result = [[0] * n for _ in range(m)]

#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 1:
#                 a[i][j] = 0
#             else:
#                 a[i][j] = 1


# def solution(key, lock):
#     # 키에서 돌기가 없는 줄은 버리고 사용할 부분만 남긴다.
#     key = ignEmpty(key)  # 상하의 빈 부분 무시
#     key = ignEmpty(rotated(key))  # 90도 돌려서 다시 상하의 빈 부분 무시
#     print(key)

#     # 자물쇠에서 필요한 부분만 남긴다
#     reverseZeroOne(lock)
#     lock = ignEmpty(lock)  # 상하의 빈 부분 무시
#     lock = ignEmpty(rotated(lock))  # 90도 돌려서 다시 상하의 빈 부분 무시
#     # 키의 돌기 수가 부족한 경우 실패
#     if sumBumps(key) < sumBumps(lock):
#         return False
#     print(lock)

#     n = len(key)
#     for l in lock:
#         cnt = 0
#         for k in key:
#             if k not in l:
#                 continue
#             cnt += 1
#             if cnt == n:
#                 return True

#     # 키를 90도씩 회전해가며 맞춰보기

#     return True


# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# print(solution(key, lock))
