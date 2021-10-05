
# ! 틀림 (15분)
# -O(N)풀이가 어떻게 되는지 모르겠어서... 실패함

# [모범답안]
# https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way

# * Kadane's algorithm
# -If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
# -If the sum is negative, it has no use to the next element, so we break.
# -it is a game of sum, not the elements.

def maxSubArray(nums) -> int:
    for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
    return max(nums)


# [내 풀이]
# ! 시간초과로 실패 O(N^2)
def maxSubArray(nums) -> int:

    data = dict()

    for i in range(len(nums)):
        data[nums[i]] = nums[i]

    for size in range(1, len(nums)+1):
        for i in range(len(nums)):
            data[nums[i]] = max(data[nums[i]], sum(nums[i: i+size]))

    return max(data.values())


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubArray(nums)
