#
# [설명]
# paragraph에서 banned, 구두점 제외하고 모두 출력
import collections
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]  # * paragraph에서 제외할 단어들

# * re.sub(r'[^\w]', " ", paragraph)
# - paragraph에서
# - 단어문자(\w)가 아닌(^) 모든 문자들을 공백으로 치환
# ? 단어문자(\w) : [A-Za-z0-9_]    영문자와 숫자 그리고 밑줄 문자

# *  .lower()
# - 모두 소문자로 변경


def common_word(paragraph):
    words = [word for word in
             re.sub(r'[^\w]', " ", paragraph)
             .lower()
             .split(" ") if word not in banned]
    # print(words)
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
    return counts.most_common(1)[0][0]


print(common_word(paragraph))
