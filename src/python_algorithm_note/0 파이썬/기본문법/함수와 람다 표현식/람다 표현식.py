# 람다식
print((lambda a, b: a+b)(2, 3))


# 자주 사용되는 예시 :

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# 람다식 사용한 경우
print(sorted(array, key=lambda x: x[1]))


# 람다식 사용하지 않은 경우 (2줄이나 더 써야됨)
# => 이런 정렬 기준 함수는 한번 쓰고 안쓰는 경우가 많은데 람다식으로 표현하면 더 간단하게 할 수 있다.
def my_key(x):
    return x[1]  # 두번째 원소 (나이)를 리턴


print(sorted(array, key=my_key))  # 정렬된 어레이 출력

print(array)  # 원본 출력
