
# ! 16진수 (hex)는 스트링으로 표현됨.
hex_number = "A"

# * 16진수 -> 10진수 : int 함수 사용
decimal_number = int(hex_number, 16)
print(decimal_number)

# * 10진수 -> 16진수 : hex 함수 사용
print(hex(decimal_number))
