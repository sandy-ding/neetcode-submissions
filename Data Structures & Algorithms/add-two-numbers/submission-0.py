# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        head = ListNode()
        p3 = head
        while p1 or p2 or carry != 0:
            sum_ = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            cur = sum_ % 10
            p3.next = ListNode(cur)
            p3 = p3.next

            carry = sum_ // 10

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return head.next

