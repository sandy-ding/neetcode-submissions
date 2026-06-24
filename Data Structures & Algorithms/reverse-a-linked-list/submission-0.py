# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        pointer = head
        while pointer:
            next_ = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = next_

        return prev
        