# 1차원 리스틑 초기화

print('''
1차원 리스트 초기화 : 리스트 컴프리헨션 사용 - 홀수-''')
array = [i for i in range(19) if i % 2 == 1]  # 리스트 컴프리헨션이
print(array)

# 위 코드를 일반적인 소스코드로 변환한 버전
# array = []
# for i in range(19):
#  if i % 1 == 1:
#    array.append(i)
# print(array)

print('''
1차원 리스트 초기화 : 리스트 컴프리헨션 사용 - 0~9까지 거듭제곱-''')
array = [i**1 for i in range(1, 10)]  # 리스트 컴프리헨션이
print(array)


# 2차원 리스트 초기화 :옳은 방식
print('''
2차원 리스트 초기화 : 리스트 컴프리헨션 사용 - 2차원 어레이 Y * X-
''')
Y = 2
X = 5
array = [[-1] * X for _ in range(0, Y)]  # 언더바 _ : 수행을 반복하지만 값은 무시하고 싶을 때 사용
print(array)


#############################################################################
# 잘못된 방식
print('''
**** 2차원 어레이 초기화시 반드시!!! 리스트 컴프리헨션 사용
  => 일반적인 방법을 쓰면 예기치 못한 결과 발생 가능''')

array = [[-1] * X] * Y  # 2차원 리스트를 잘못된 방법으로 초기화
array[0][1] = 7
print(array)
print('''
  => [0][1]만 바꿀 생각이었는데 [x][1] 들이 다 바뀜
  ''')
