

# [입력]
# - paragraph
# - banned

# [return]
#  - the most frequent word that is not banned.


from collections import Counter
import re


def mostCommonWord(paragraph: str, banned) -> str:

    paragraph = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

    count = Counter(paragraph)

    # count.most_common(n) 상위 n개 단어 선택

    return count.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
mostCommonWord(paragraph, banned)
