from itertools import combinations, combinations_with_replacement, permutations, product


data = ['A', 'B', 'C']

# *순열 : 순서를 고려하여 n개에서 r개 선택
# (A,B)와 (B,A)는 다른 것으로 취급한다
result = list(permutations(data, 2))
print(result)

# *조합 : 순서를 고려하지 x,  n개에서 r개 선택
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
