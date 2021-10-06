
# * 정답 (10분)
# - 그래프 서치라.. 뭐 딱히 개선할 건 없는듯? 코드 길이 줄이는 정도?
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, cur: Optional[TreeNode]):
        data = []
        if cur:
            data.append(cur.val)
            data += self.bfs(cur.left)
            data += self.bfs(cur.right)
        else:
            data = ['null']
        return data

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_data = self.bfs(p)
        q_data = self.bfs(q)

        return p_data == q_data
