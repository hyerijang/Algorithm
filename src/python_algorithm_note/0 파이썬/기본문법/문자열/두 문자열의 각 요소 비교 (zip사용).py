# https://docs.python.org/ko/3/library/functions.html#zip

# [두문자열의 각 요소를 비교하여 동일하지 않은 문자 개수 카운트]
current = "apple"
word = "Apple"

count = 0
for c, w in zip(current, word):
    if c != w:
        count += 1

print(f"{count}개의 요소가 동일하지 않음")


# ! 두 문자열의 길이가 다른경우 짧은 것을 기준으로 맞춰진다.
current = "aaaa"
word = "aaaaaaa"
count = 0
for c, w in zip(current, word):
    if c != w:
        count += 1
print(f"{count}개의 요소가 동일하지 않음")


# * zip()을 * 연산자와 함께 쓰면 리스트를 unzip 할 수 있습니다:
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

x2, y2 = zip(*zip(x, y))  # - unzip
print(x == list(x2) and y == list(y2))
