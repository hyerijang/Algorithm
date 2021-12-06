# https://leetcode.com/problems/two-sum/

from typing import List

num_list = List[int]


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complment = target - n
        if complment in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complment) + (i+1)]


nums = [2, 7, 11, 15]
twoSum(nums, 9)
