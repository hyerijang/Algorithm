# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2


# 1000명의 수학성적 -> 통계
# 최빈수 : 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.


# 테스트케이스 개수 : T
from collections import Counter

t = int(input())

Cnt = Counter # 속도 향상 위해 재정의

for _ in range(t):
    print(f"#{int(input())} {Cnt(map(int, (input().split()))).most_common(1)[0][0]}")
