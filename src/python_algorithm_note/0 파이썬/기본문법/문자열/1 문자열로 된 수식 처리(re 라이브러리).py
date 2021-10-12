import re
# [기호, 숫자 구분]
# * re.split(pattern, string)
# -pattern을 괄호로 감싸는 경우, pattern에 해당하는 부분문자열도 결과 리스트에 포함된다.

s = "1+2*99"
data = re.split('(\D)', s)  # ! "(\D)" => 기호 포함
print(data)

data_only_num = re.split('\D', s)  # ! "\D" => 기호 제외
print(data_only_num)

# [문자열로 된 수식 계산]
print(eval(s))
