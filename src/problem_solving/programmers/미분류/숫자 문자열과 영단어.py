# https://programmers.co.kr/learn/courses/30/lessons/81301
# 정답

english_word = dict()

english_word['zero'] = 0
english_word['one'] = 1
english_word['two'] = 2
english_word['three'] = 3
english_word['four'] = 4
english_word['five'] = 5
english_word['six'] = 6
english_word['seven'] = 7
english_word['eight'] = 8
english_word['nine'] = 9


def solution(s):
    answer = ""

    key_list = english_word.keys()
    while len(s) > 0:
        # print(answer, s)
        if s[0].isdecimal():
            answer += s[0]
            s = s[1:]
            continue

        else:
            for key in key_list:
                if s[0:3] in key[0:3]:
                    s = s[len(key):]
                    answer += str(english_word[key])
                    break

    return int(answer)


print(solution("2three45sixseven"))
