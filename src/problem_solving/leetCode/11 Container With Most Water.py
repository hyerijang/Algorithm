def maxArea(height):
    left, right = 0, len(height) - 1

    answer = 0
    while left < right:
        cur = (right - left) * min(height[left], height[right])
        answer = max(answer, cur)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return answer


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(height))
