
# * 정답 (10분)

# [모범답안]
# https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34345/Python-BFS-solution
# - 오. 같은 레벨에 있는건  level에 저장할 수도 있구나
# ! queue랑 level을 분리한 이유?
# - 매 레벨이 시작될때 queue= [] 로 초기화 하므로써 이전 레벨의 노드에 대해서는 무시함
# - deque로 구현하고 popleft로 대체 할수도 있었겠지만.. 이게 더 보기 편하긴 하다.

from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []  # At every level, []로 초기화

            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            # * 같은 레벨에 있는 모든 노드는 level 로 별도 저장
            #  - We increase the depth till the time "queue" is an empty list.
            level = queue

        return depth


# [내코드]
# - 평균보다 느리지만 메모리는 적게 씀
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = -1

        queue = deque()

        queue.append((0, root))
        while queue:
            cur = queue.popleft()
            depth = cur[0]
            node = cur[1]

            max_depth = max(max_depth, depth)

            if cur[1] != None:
                queue.append((depth + 1, cur[1].left))
                queue.append((depth + 1, cur[1].right))

        return max_depth
