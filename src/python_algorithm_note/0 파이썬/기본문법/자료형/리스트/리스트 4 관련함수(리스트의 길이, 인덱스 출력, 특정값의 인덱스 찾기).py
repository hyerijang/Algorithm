nums = [2, 3, 24, 9, 11, 57, 9, 8, 1, 0, 23, 42, 6, 78, 768, 546, 456]

# 리스트 길이
print('길이', len(nums))


# enumerate 사용하여 리스트의 순서와 값을 리턴한다.
for i, n in enumerate(nums):
    # 리스트의 인덱스 i
    # nums[i] 의 값 n
    print(i, n)


# * 리스트 내에서 특정 값의 인덱스 찾기
# (method) index: (__value: int, __start: SupportsIndex = ..., __stop: SupportsIndex = ...) -> int
# Return first index of value.
# Raises ValueError if the value is not present.
nums = [1, 1, 1, 1, 5]

i = nums.index(1)
print("index=", i)

i = nums.index(1, 3)  # start : 3번 인덱스
print("index=", i)
