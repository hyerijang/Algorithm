list = [0]


# [삽입]
# * 리스트의 마지막에 삽입
list.append(1)
print(list)

# * 특정 인덱스에 삽입
# * insert(인덱스, 삽입할 값) : 특정 위치에 원소 삽입하고, 원래 있던 값들은 한칸씩 미룸
list.insert(9, 333)
list.insert(0, -1)
print(list)

# [삭제]
# * remove(지울 값) : 값이 여러개일 경우 가장 먼저 나오는 값을 지우고, 원래 있던 값들 한칸씩 당김
list.remove(-1)
print(list, "-1 삭제")

# ? 시간 복잡도 -삽입 삭제
# - append O(1)
# - insert O(N) #주의해서 사용!
# - remove O(N)


a = [1, 2, 3, 4, 5]
remove_set = [3, 4]


# ! 파이썬은 remove all 지원 x
# ! 특정 원소 제외 시 리스트 컴프리헨션 응용


# [특정 원소 제외 (리스트 컴프리헨션)]
result = [i for i in a if(i not in remove_set)]
print(result)

# [특정 원소 제외 (일반 버전)]
result = []
for i in a:
    if(i not in remove_set):
        result.append(i)
print(result)
