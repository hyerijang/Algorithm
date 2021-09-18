# 단순하게 구현한 버전
# m이 100억개 이상인 경우 수행속도 초과됨
# 개선 버전 참고할것

from re import I


n, m, k = map(int, input().split())


arr = list(map(int, input().split()))

arr.sort(reverse=True)  # 역순 정렬

# print(arr)

result = 0
while True:
    for _ in range(k):  # 가장 큰 수를 k번 더한다
        if m == 0:
            break
        result += arr[0]
        m -= 1

    if m == 0:
        break

    result += arr[1]  # 두번째 큰 수를 한번 더한다
    m -= 1

print(result)
