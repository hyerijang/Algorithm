# #데이터의 개수 입력
import sys
n = int(input())

# #리스트의 형태로 정수 데이터 입력받음
# #공백 ' '을 기준으로 입력
data = list(map(int, input().split()))
# map 함수 : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다.

data.sort(reverse=True)

print(n)
print(data)


n = 3
print(str(n) + " 입니다")
print(n, " 입니다")  # 예기치 못한 공백 보함될 수 있음!
print(f"{n} 입니다")  # python 3.6 이상
