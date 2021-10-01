# 리스트를 사용!!
# 삽입 : append(i)
# 삭제 : pop()

stack = []

stack. append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

# pop(인덱스) 하면 해당 인덱스의 데이터 pop한다.
data = stack.pop()  # stack.pop(-1)와 같음
print(stack, "          popped data=", data)


stack.append(99)
stack.append("latest")


print(stack)
print(stack[::-1])  # 가장 마지막에 들어온 애부터 출력
