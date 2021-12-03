# 그룹 애너그램

# - Given an array of strings strs, group the anagrams together.
# - You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# str :  영어 소문자만 포함

from collections import defaultdict
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


data = defaultdict(list)
for str in strs:
    s = "".join(sorted(str))
    data[s].append(str)

# result = [sorted(x) for x in data.values()]
print(data.values())
