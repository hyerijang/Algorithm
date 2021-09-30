# 유클리드 호제법
# 최대 공약수 찾기
def gcb(a, b):
    if (a % b == 0):
        return b
    else:
        return gcb(b, a % b)


print(gcb(192, 162))
print(gcb(162, 192))  # a,b의 순서는 상관 없음
