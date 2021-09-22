# https://leetcode.com/problems/roman-to-integer/

dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

# 모범답안
# https://leetcode.com/problems/roman-to-integer/discuss/6542/4-lines-in-Python


def romanToInt(s: str) -> int:
    res = 0
    p = 'I'

    for c in s[::-1]:
        if dic[c] < dic[p]:
            res -= dic[c]
        else:
            res += dic[c]
            p = c

    print(res)
    return res


# count = {}
# count['I'] = 0
# count['V'] = 0
# count['X'] = 0
# count['L'] = 0
# count['C'] = 0
# count['D'] = 0
# count['M'] = 0
# def romanToInt(s: str) -> int:
#     for i in s:
#         count[i] = count[i] + 1

#     result = 0
#     # 1의 자리
#     result += count['V'] * dic['V']
#     if count['V'] > 0:
#         result -= count['I']
#     else:
#         result += count['I']

#     # 10의 자리
#     result += count['L'] * dic['L']
#     if count['L'] > 0:
#         result -= count['X'] * dic['X']
#     else:
#         result += count['X'] * dic['X']

#     # 100의 자리
#     result += count['D'] * dic['D']
#     if count['D'] > 0:
#         result -= count['C'] * dic['C']
#     else:
#         result += count['C'] * dic['C']

#     # 1000의 자리
#     result += count['M'] * dic['M']

#     # print(count)
#     return result


s = "IV"
print(romanToInt(s))
