# https://leetcode.com/problems/two-sum/
# 책에 있는 풀이는  Input: nums = [3,3], target = 6 같은 조건 고려하지 x

# [모범답안]
# https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation

# [내풀이]
# * 79ms, (2021/12/15)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        data = dict()
        for idx, value in enumerate(nums):
            if data.get(value) == None:
                data[value] = []
            data[value].append(idx)

        for n in nums:

            if n * 2 == target and len(data.get(n)) < 2:
                continue

            if data.get(target - n) != None:
                return [data[target - n].pop(), data[n].pop()]

        raise ValueError


# --------------------- 테스트--------------------
nums = [3, 3]
target = 6

s = Solution()

print(s.twoSum(nums, target))
