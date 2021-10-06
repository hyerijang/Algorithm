
# * 정답 (20분)

# [모범답안]
# https://leetcode.com/problems/symmetric-tree/discuss/33057/Python-iterative-way-using-a-queue
# * 큐를 사용한다
# ! node1.left and node2.right are symmetric nodes in structure
# ! node1.right and node2.left are symmetric nodes in structure
# - 큐 사용한 코드중에 더 짧은거 있는데 내 뇌가 거부함 ^^.. (https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python)


class Solution:
    # @param root, a tree node
    # @return a boolean


def isSymmetric(self, root):
    if not root:
        return True

    dq = collections.deque([(root.left, root.right), ])
    while dq:
        node1, node2 = dq.popleft()
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        # node1.left and node2.right are symmetric nodes in structure
        # node1.right and node2.left are symmetric nodes in structure
        dq.append((node1.left, node2.right))
        dq.append((node1.right, node2.left))
    return True


# [내 코드]
# - 시간 내에 동작하긴 하는데 평균에 비해 매우 느린편이고, 메모리도 많이 사용함
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getList(self, cur: Optional[TreeNode]):

        data = []
        if cur:
            data += [cur.val]
            data += self.getList(cur.left)
            data += self.getList(cur.right)
        else:
            data = ['null']

        return data

    def getmirrorList(self, cur: Optional[TreeNode]):

        data = []
        if cur:
            data += [cur.val]
            data += self.getmirrorList(cur.right)
            data += self.getmirrorList(cur.left)
        else:
            data = ['null']

        return data

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.getList(root.left) == self.getmirrorList(root.right)
