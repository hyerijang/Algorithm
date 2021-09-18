def add(a, b):
    print(a+b)


# 파라미터의 변수를 직접 지정 가능
#    이 경우 매개변수의 순서가 달라도 상관 x
add(b=15, a=111)


a = "함수 바깥에 선언된 a입니다"
# global 키워드


def func():
    global a  # 함수 바깥에 선언된 a를 참조하기 위해선 global을 사용해야함
    print(a)


func()
