def add(a, b):
    return a+b


print(add(1, 4))


# 같은 이름의 함수 여러개면 최근 정의된 것을 호출
def add(a, b):
    print(a+b)


add(111, 15)
