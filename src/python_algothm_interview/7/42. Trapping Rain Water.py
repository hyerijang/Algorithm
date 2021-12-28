from typing import List


class Solution:
    # 투포인터
    def trap(self, height: List[int]) -> int:
        volume = 0

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max-height[left]
                left += 1

            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    # 스택 - 어려움
    def trap_stack(self, height: List[int]) -> int:
        volume = 0
        stack = []

        for idx in range(len(height)):

            # 변곡점을 만나는경우
            while stack and height[idx] > height[stack[-1]]:
                # 스택에서 꺼낸다.
                top = stack.pop()

                # 물이 고일 수 없는경우 break
                if not stack:
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = idx - stack[-1] - 1
                water = min(height[idx], height[stack[-1]]) - height[top]
                # print(
                #     f"변곡점 = {idx}, volume = {volume} + {distance} * {water} ", )
                volume += distance * water

            stack.append(idx)

        return volume

    def print_trap(self, height: List[int]) -> None:
        # print(self.trap(height))
        print(self.trap_stack(height))


# --------------------- 테스트--------------------
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


s = Solution()
s.print_trap(height)
