# https://programmers.co.kr/learn/courses/30/lessons/42578
# ! 틀림 (25분)
# - 쓸데없이 복잡하게 생각했다

# * 풀이 https://eda-ai-lab.tistory.com/472
# -각 종류별 count를 계산
# -계산한 count를 통해서 (count+1)를 곱해주고 마지막에 1을 빼줌
# ! 1을 빼주는 이유는 모두 안입은 경우를 제거

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1


clothes = [["yellowhat", "headgear"],
           ["bluesunglasses", "eyewear"],
           ["green_turban", "headgear"]]

solution(clothes)
