# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # ㅍㅍ
    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        # ㄹㄹ
        # left가 비어있으면 right 와 변경
        # left 가 차있는데 right 가 비어있으면
        # left의 값은 더 작아야함
        if (not left) or (right and left.val > right.val):
            left, right = right, left

        if left:
            left.next = self.mergeTwoLists(left.next, right)

        return left
