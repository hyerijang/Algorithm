
# [포함하고 있는 문자열 종류 검사]
# *숫자인지 확인하기(isdigit)
print("1".isdecimal())

# *알파벳인지 확인하기(isalpha)
print("a".isalpha())

# *알파벳 또는 숫자인지 확인하기(isalnum)
print("a1".isalnum())


# [문자열 대소문자 검사]

# * 소문자 (islower)
print('abc123!@#'.islower())
# True ==> 알파벳만 검사하므로 숫자나 특수문자는 무시한다.

# * 대문자 (isupperr)
print('Abc'.isupper())  # 대문자인지 검사
# False ==> 모든 알파벳이 대문자여야 True
