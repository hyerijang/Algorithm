nums = [2, 3, 24, 9, 11, 57, 9, 8, 1, 0, 23, 42, 6, 78, 768, 546, 456]

# 리스트 길이
print('길이', len(nums))


# enumerate 사용하여 리스트의 순서와 값을 리턴한다.
for i, n in enumerate(nums):
    # 리스트의 인덱스 i
    # nums[i] 의 값 n
    print(i, n)
