# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# =========== 풀이 1 재귀 구조로 뒤집기 ===========
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:  # 노드가 비어있으면
                return prev  # prev 리턴 (정답)

            # 노드가 비어있지 않은 경우
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)
