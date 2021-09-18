# 집합 { }
# 중복을 허용하지 않고
# 순서가 없다 : 인덱싱으로 값을 얻을 수 없다.
# 특정 원소가 존재하는 지 검사 : O(1) 소요

# 초기화 1. set함수 이용
data = set([1, 2, 3])
print(data)
# 초기화 2. 중괄호 이용
data2 = {3, 4}
print(data2)

print("\n합집합")
print(data | data2)
print("차집합")
print(data-data2)
print("교집합")
print(data & data2)


print("\n집합에 1개 원소 추가 /삭제 : O(n)")
data.add(0)  # 1개 추가 : O(1)
print(data)
data.remove(1)  # 1개 삭제 : O(1)
print(data)


print("\n집합에 여러개 원소 추가 ")
data.update([1, 2, 3, 4, 5])  # 여러개 추가
print(data)
