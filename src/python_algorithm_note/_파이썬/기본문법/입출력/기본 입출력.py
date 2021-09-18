# #데이터의 개수 입력
import sys
n = int(input())

# #리스트의 형태로 정수 데이터 입력받음
# #공백 ' '을 기준으로 입력
data = list(map(int, input().split()))

data.sort(reverse=True)

print(n)
print(data)


# 빠르게 입력받아야 할때
# sys.stdin.readline().rstrip() 사용 (1줄씩 입력)

text = sys.stdin.readline().rstrip()

print("\n출력")
print(text)


n = 3
print(str(n) + " 입니다")
print(n, " 입니다")  # 예기치 못한 공백 보함될 수 있음!
print(f"{n} 입니다")  # python 3.6 이상
