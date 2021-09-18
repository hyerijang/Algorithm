from itertools import combinations, combinations_with_replacement, permutations, product


data = ['A', 'B', 'C']

# 순열 : 순서를 고려하여 n개에서 r개 선택
result = list(permutations(data, 2))
print(result)

# 조합 : 순서를 고려하지 x n개에서 r개 선택
result = list(combinations(data, 2))
print(result)

# 중복 순열
result = list(product(data, repeat=2))  # 반복 횟수 repeat = 2 로 명시해야함
print(result)


# 중복 조합
result = list(combinations_with_replacement(data, 2))
print(result)
