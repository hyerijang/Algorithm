def trap(height) -> int:
    answer = 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            answer += left_max - height[left]
            left += 1
        else:
            answer += right_max - height[right]
            right -= 1

    return answer


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
