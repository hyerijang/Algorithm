# 로그파일 재정렬

# log가 주어진다
# [log]
# - 공백이 제거된 string of words.
# - 첫번째 단어는 *식별자*

def reorderLogFiles(logs):

    digits = []
    letters = []

    # (식별자를 제외) 로그가 문자 로그인지 숫자로그인지 확인
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


# logs = ["dig1 8 1 5 1",
#         "let1 art can",
#         "dig2 3 6",
#         "let2 own kit dig",
#         "let3 art zero"]

# output = ["let1 art can", "let3 art zero",
#           "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

# print(reorderLogFiles(logs) == output)
