
# ! 사전 자료형 : 해시테이블로 응용
# ! 파이썬 3.6이전에는 입력순서 유지 x (=> OrderedDict 사용해야함.)
# 데이터의 검색, 수정에 O(1) 걸림
# 키 - 값 쌍으로 이루어진 데이터에 대해 리스트보다 빨리 동작한다.

# [초기화]
#! 키에는 리스트, 딕셔너리 사용 불가
# * 초기화 1 : dict 함수
import collections
data = dict()
# * 응용
# - 딕셔너리 = dict(키1=값1, 키2=값2)
# - 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
# - 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
# - 딕셔너리 = dict({키1: 값1, 키2: 값2})

data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['바나나'] = 'Banana'


# *초기화 2 : 중괄호
dict1 = {'X': 2, 'Y': 3, 'Z': 4}
print(dict1)

print(data)

# [데이터의 검색]
if '사과' in data:
    print("사과 있음")

# [키 리스트, 값 리스트, 둘다 추출]
key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)
item_list = data.items()
print(item_list)

# * 키 리스트 응용 : 각 키에 따른 값을 전부 출력
for key in data:
    print(data[key])
