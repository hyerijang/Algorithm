# https://leetcode.com/problems/3sum/
# 모범답안 O(n²).
# https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation


# 단순히 for문 3번 겹치는 방식 쓰면 시간 초과 발생함


# O(n²).
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # 정렬!
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:  # 중복 제거
                continue
            target = nums[i]*-1  # target 은  nums[i]
            s, e = i+1, N-1  # s는 왼쪽 끝, e는 오른쪽 끝에서 시작
            while s < e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s < e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1  # s를 늘린다
                else:  # 두 값의 크기가 target 보다 크면
                    e = e-1  # e의 인덱스를 줄인다 (더 작은 값 가리키게 함)
        return result


nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
print(solution.threeSum(nums))
