# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pointer = head
        for i in range(n):
            if pointer:
                pointer = pointer.next
        
        pointer2 = dummy
        while pointer:
            pointer = pointer.next
            pointer2 = pointer2.next

        pointer2.next = pointer2.next.next
        return dummy.next