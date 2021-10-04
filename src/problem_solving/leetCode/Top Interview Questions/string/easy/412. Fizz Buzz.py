
# * 정답 (10분) 쉬웠음.
# - 더 나은 풀이는 딱히 없는 듯

def fizzBuzz(n: int):
    answer = []
    for i in range(1, n+1):
        s = ""
        if i % 3 == 0:
            s = "Fizz"
        if i % 5 == 0:
            s += "Buzz"

        if s == "":
            s += str(i)

        answer.append(s)

    return answer


print(fizzBuzz(5))
