u = "123456"

# 문자열을 리스트로 변환
u = list(u)

# 값 변경
u[0] = '0'

# 리스트를 문자열로 변환
answer = "".join(u)

print(answer)
