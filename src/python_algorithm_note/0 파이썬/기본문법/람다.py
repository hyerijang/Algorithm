
# ? 람다식
#  [표현] lambda 인자 : 표현식
# - 람다식 O
from functools import reduce
(lambda x, y: x + y)(10, 20)


# - 람다식x
def hap(x, y):
    return x + y


hap(10, 20)


# [람다 응용]
# (맵)
# * list(map(함수, 리스트))
# -리스트 내의 원소에 대하여 함수를 적용, 결과를 리스트로 반환한다.
# list(map(함수, range(5)))
list(map(lambda x: x ** 2, range(5)))  # [0, 1, 4, 9, 16]

# (누적집계 (reduce()))
# from functools import reduce   # 파이썬 3에서는 써주셔야 해요
reduce(lambda x, y: y + x, 'abcde')  # 'edcba', #! 리스트 안붙여도됨 ,  해당하는 자료형으로 반환
print(reduce(lambda x, y: y + x, 'abcde'))

# (필터)
# * list(filter(함수, 리스트))
# - 리스트 내의 원소에 대하여 함수를 적용, 리턴값이 True인 결과들을 리스트로 반환한다.
list(filter(lambda x: x < 5, range(10)))
