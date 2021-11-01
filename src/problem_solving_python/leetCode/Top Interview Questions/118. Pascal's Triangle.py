# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/submissions/

# *정답 (16분)
# - 어렵진 않았는데 리스트 컴프리헨션으로 풀어보려고 하다보니까 좀 시간 걸렸네
# - 근데 리스트 컴프리헨션 안쓰는게 더 가독성이 좋았을거란 생각이 든다. 더 쉽기도 하고.


# [모범답안1]
# https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
# ! 이건 또... 신박한 풀이네 (링크 내 설명 참조)

def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]

# [모범답안2]
# - 내 코드보다 가독성이 더 좋다.
# - 시간복잡도는 비슷


def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal


# [내 답안]
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 파스칼의 삼각형
        # 특정 행의 [0], [-1]은 무조건 1
        # [1:-2] 번째 열 => idx
        # 이전 행의 [idx -1] + [idx] 값을 더한다

        result = []
        for i in range(numRows):
            col = [result[i-1][k] + result[i-1][k-1]
                   if i > 0 and k != 0 and k != i
                   else 1
                   for k in range(i+1)]
            result.append(col)
        return result
