from collections import Counter

# 등장 횟수 세기 : Counter 이용
counter = Counter(['red', 'green', 'blue', 'blue'])

print(counter['red'])
print(counter['green'])
print(counter['blue'])


# 등장횟수를 딕셔너리로 만들기 *********
print(dict(counter))

# ! 리스트의 두번째 요소를 기준으로 카운트하는 법
# clothes = [  [name, kind],[name2, kind2],[name3, kind3] ]

data = Counter([kind for name, kind in clothes])

# * 아래 코드를 위의 한줄로 대체 가능
# clothes_type = [] #의상의 종류만 저장 (중복o)
# for c in clothes :
#     clothes_type.append(c[1])

# data = Counter(clothes_type)  # 종류별 의상 개수 카운트
