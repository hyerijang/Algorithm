# 순열 구현 : DFS
def permutaion(nums: list, k):
    result = []
    previous_element = []

    def dfs(elements, k):
        if k == 0:
            result.append(previous_element[:])
            return

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            previous_element.append(e)
            dfs(next_elements, k - 1)
            previous_element.pop()

    dfs(nums, 4)

    return result


li = [1, 2, 3, 4]
print(f"순열:{permutaion(li, 2)}")


# 조합
# elements를 입력받아 k개의 조합을 리턴
def combination(elements: list, k: int):
    result = []
    n = len(elements)

    def dfs(previous_elements: list, start: int, k: int):
        if k == 0:
            result.append(previous_elements[:])
            return

        for idx in range(start, n):
            previous_elements.append(elements[idx])
            dfs(previous_elements, idx + 1, k - 1)
            previous_elements.pop()

    dfs([], 0, k)

    return result


print(f"조합:{combination(['a', 'b', 'c', 'd'], 2)}")

