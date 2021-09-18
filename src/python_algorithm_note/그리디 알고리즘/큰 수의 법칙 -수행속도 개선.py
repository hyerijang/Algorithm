from re import I

# 개선된 버전에서는 아래 반복문을 없애고 수학적인 계산을 이용

n, m, k = map(int, input().split())


arr = list(map(int, input().split()))

arr.sort(reverse=True)  # 역순 정렬

# print(arr)

first = arr[0]
second = arr[1]


result = 0
# while True :
#     for _ in range(k) : # 가장 큰 수를 k번 더한다
#         if m == 0:
#             break
#         result += arr[0]
#         m -= 1

#     if m == 0:
#         break

#     result += arr[1] #두번째 큰 수를 한번 더한다
#     m-=1


# first가 등장하는 횟수 : count
count = (m//(k+1) + m % (k+1)) * k
# print(count)
# second가 등장하는 횟수 : m-count
# print(m-count)


result += count*first
result += (m-count) * second
print(result)
