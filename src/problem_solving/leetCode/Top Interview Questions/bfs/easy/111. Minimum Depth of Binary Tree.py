
# * 정답(15분)

# [내 답안]
# - BFS 로 풀었음.
# - 다른사람들은 deque써서 푼듯? 근데 로직은 비슷해.
# - 시간복잡도가 하위 13프로라서 좀 그러네

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        level = [root]
        depth = 0

        li = []
        while level:
            depth += 1
            queue = []

            for v in level:
                if v != None:
                    if v.left == None and v.right == None:
                        li.append(depth)
                    else:
                        queue.append(v.left)
                        queue.append(v.right)

            level = queue

        if li == []:
            return 0

        return min(li)
