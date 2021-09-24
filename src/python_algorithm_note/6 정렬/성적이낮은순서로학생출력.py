# 3
# 홍길동 96
# 이순신 70
# 세종대왕 100


#  N 입력 받기
n = int(input())

# N명의 학생 정보를 입력 받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 학생 정보를 (이름,점수)로 묶어 튜플로 저장
    # 왜 튜플?
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
# - 람다식을 사용해서 키를 지정하였다.
# - (이름, 점수)이므로 student[1]은 점수이다.
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')
