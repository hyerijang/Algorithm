# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# [정답] (58분)
# - ??? 왜이렇게 오래걸렸지
# (1) 우선 inorder 이 뭔지 까먹음 (!중위순회!)
# (2) 릿코드 ide로 풀었음. 자동안성 안되니까 너무 불편하네.

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    if root != None:
        result += self.inorderTraversal(root.left)
        result += [root.val]
        result += self.inorderTraversal(root.right)
    return result

# [순회]
# - 부모노드를 언제 방문하느냐에 따라 중위/전위/후위로 구분
# * inorder(중위 순회) : 왼쪽자식 -> *부모* -> 오른쪽 자식
# * preorder(전위 순회) :  *부모* -> 왼쪽자식 ->오른쪽 자식
# * postorder(후위 순회) : 왼쪽자식 ->오른쪽 자식 ->*부모*
