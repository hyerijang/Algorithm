# 사전 자료형 : 해시테이블로 응용
# 데이터의 검색, 수정에 O(1) 걸림
# 키 - 값 쌍으로 이루어진 데이터에 대해 리스트보다 빨리 동작한다.

# 초기화 : dict 함수
data = dict()

data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['바나나'] = 'Banana'

print(data)

# 데이터의 검색
if '사과' in data:
    print("사과 있음")

key_list = data.keys()
print(key_list)
value_list = data.values()
print(value_list)

# 각 키에 따른 값을 전부 출력
for key in data:
    print(data[key])
