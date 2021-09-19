# 이코테 p113
# 예제 4-2 시각
n = 5

result = 0

for h in range(n+1):
    for m in range(60):  # 0~59 에 3이 든 경우의 수 구하기

        for s in range(60):
            if '3' in str(h)+str(m)+str(s):  # 문자열 안에 '3'이 있는지 검사!!!!!!!!!
                result += 1

print(result)
