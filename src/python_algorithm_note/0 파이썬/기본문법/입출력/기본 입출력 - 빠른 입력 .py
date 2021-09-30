# 빠르게 입력받아야 할때
# sys.stdin.readline().rstrip() 사용 (1줄씩 입력)

# readline() 사용시 오른쪽 끝에 줄바꿈 기호 삽입됨
# .rstrip()? 가장 오른쪽의  줄바꿈 기호(엔터) 제거


import sys

text = sys.stdin.readline().rstrip()

print("\n출력")
print(text)
