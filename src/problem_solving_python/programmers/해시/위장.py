# https://programmers.co.kr/learn/courses/30/lessons/42578
# * 정답 (20분)
# 원래 이상하게 풀다가 생각나서 맞춤!
def solution(clothes):
    clothes_type = []  # 의상의 종류만 저장 (중복o)
    for c in clothes:
        clothes_type.append(c[1])

    data = Counter(clothes_type)  # 종류별 의상 개수 카운트

    count_list = data.values()

    answer = 1
    for count in count_list:
        answer *= (count+1)  # 해당 종류의 옷을 안입는 경우도 카운트

    # 모든 종류의 의상 안 입는 경우는 제외
    answer -= 1

    return answer

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
