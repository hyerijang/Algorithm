# 리스트를 사용!!
# 삽입 : append(i)
# 삭제 : pop()

stack = []

stack. append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.append(1)
stack.append("latest")


print(stack)
print(stack[::-1])  # 가장 마지막에 들어온 애부터 출력
