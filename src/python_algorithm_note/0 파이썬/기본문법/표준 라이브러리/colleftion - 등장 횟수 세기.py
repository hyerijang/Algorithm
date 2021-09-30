from collections import Counter

# 등장 횟수 세기 : Counter 이용
counter = Counter(['red', 'green', 'blue', 'blue'])

print(counter['red'])
print(counter['green'])
print(counter['blue'])


# 등장횟수를 딕셔너리로 만들기 *********
print(dict(counter))
