# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV_6mRsasV8DFAWS&categoryId=AV_6mRsasV8DFAWS&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3#none
# 100만 이하의 모든 소수

MAX = 1000000

li = [True for _ in range(MAX + 1)]
li[0] = li[1] = False

for num in range(2, MAX + 1):
    if li[num] == True:
        for non_prime_num in range(num * 2, MAX + 1, num):
            li[non_prime_num] = False

result = [num for num, is_prime_num in enumerate(li) if is_prime_num]

for num in result[:-1]:
    print(num, end=" ")
print(result[-1], end="")
