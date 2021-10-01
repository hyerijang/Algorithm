# 탐욕법 Level 1
# https://programmers.co.kr/learn/courses/30/lessons/42862

# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# * 체육수업을 들을 수 있는 학생의 최댓값 리턴
def solution(n, lost, reserve):

    student = [0]+[1]*n

    for i in range(1, n+1):
        if i in lost:  # 체육복 잃어버린 경우
            student[i] -= 1
        if i in reserve:  # 여분이 있는 경우
            student[i] += 1

    for i in range(1, n+1):
        print(student)
        if student[i] == 2:  # 여벌 체육복이 있는 경우
            if i != 1 and student[i-1] == 0:  # 앞 번호 학생 우선하여 빌려줌
                student[i] -= 1
                student[i-1] += 1

        if student[i] == 2:  # 여벌 체육복이 있는 경우
            if i != n and student[i+1] == 0:  # 앞 번호가 체육복 있으면 뒷번호에게 빌려줌
                student[i] -= 1
                student[i+1] += 1

    answer = student.count(1) + student.count(2)
    # print(answer, student)
    return answer


# 입출력 예
n,	lost,	reserve	, return_value = 5,	[2, 4],	[1, 3, 5],	5
print(return_value == solution(n, lost, reserve))

n,	lost,	reserve	, return_value = 5,	[2, 4],	[3], 4
print(return_value == solution(n, lost, reserve))

n,	lost,	reserve	, return_value = 3,	[3],	[1],	2
print(return_value == solution(n, lost, reserve))
