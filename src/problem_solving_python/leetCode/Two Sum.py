# 모범 답안
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            print(i, n)
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

# 내 답

# class Solution:
#     def twoSum(self, nums, target: int):
#         # print(len(nums))
#         result = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 if nums[i] + nums[j] == target:
#                     result.append(i)
#                     result.append(j)
#                     return result


nums = [2, 7, 11, 15]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))
