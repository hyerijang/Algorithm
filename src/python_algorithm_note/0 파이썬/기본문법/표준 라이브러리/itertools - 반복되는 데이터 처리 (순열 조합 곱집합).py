from itertools import combinations, combinations_with_replacement, permutations, product


data = ['A', 'B', 'C']

# *순열 : 순서를 고려하여 n개에서 r개 선택
# (A,B)와 (B,A)는 다른 것으로 취급한다 //순서를 고려한다.
result = list(permutations(data, 2))
print(result)

# *조합 : 순서를 고려하지 않고  n개에서 r개 선택
# (A,B)와 (B,A)를 같은 것으로 취급
result = list(combinations(data, 2))
print(result)

# [중복~~]
# (A,A) 처럼 같은 인덱스의 요소가 2번나올 수 있다.

# * 중복 순열
result = list(product(data, repeat=2))  # 반복 횟수 repeat = 2 로 명시해야함
print(result)


# *중복 조합
result = list(combinations_with_replacement(data, 2))
print(result)


# [곱집합] Catesian product
# -여러 집합들 간에 하나씩 뽑아 조합을 만들 수 있는 모든 경우
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

# 리스트 a와 b에서 각각 1개씩 뽑는다. => 각각의 조합은 튜플로 표현됨
result = product(list_a, list_b)
print(list(result))

# * 곱집합 응용 => DFS문제 (프로그래머스- 타겟넘버)
l = [(x, -x) for x in [1, 2, 3]]
# s는 [(-1,1),(-2,2),(-3,3)]내의 각각의 튜플에서 하나씩 뽑아 조합을 만든다.
s = list(product(*l))  # ! l안에 있는 튜플을 꺼내 쓰는 것이므로 *l 임에 주의한다.
print(s)
