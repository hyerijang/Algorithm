# https://leetcode.com/problems/valid-parentheses/
def isValid(s):
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():  # char 가 여는 괄호이면
            stack.append(char)
        elif char in dict.keys():  # char 가 닫는 괄호이면
            if stack == [] or dict[char] != stack.pop():  # stack이 비어있거나 이전 괄호와 짝이 맞지 않는 괄호가 들어온 경우
                return False
        else:  # char 가 위에 해당하는 괄호가 아니면
            return False
    return stack == []


# 내 풀이 : 틀림
def isValid(s: str) -> bool:

    data = {"]": "[", "}": "{", ")": "("}
    stack = []

    for char in s:
        if char in data.values():  # 여는 괄호이면
            stack.append(char)

        elif char in data.keys():  # 닫는 괄호이면
            if stack == []:
                return False
            elif data[char] == stack.pop():
                answer = True
            else:
                return False

    return stack == []


# s = "()"
# print(s, isValid(s))

# s = "()[]{}"
# print(s, isValid(s))

# s = "{[]}"
# print(s, isValid(s))

# s = "{"
# print(s, isValid(s))

# s = "}"
# print(s, isValid(s))

s = "([]){"
print(s, isValid(s))
