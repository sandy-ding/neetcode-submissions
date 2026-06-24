# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find middle point
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse the second half
        pointer_1 = slow
        pointer_2 = None
        while pointer_1:
            temp = pointer_1.next
            pointer_1.next = pointer_2
            pointer_2 = pointer_1
            pointer_1 = temp

        # 3. merge the list
        pointer_1 = head
        while pointer_1 and pointer_2 and pointer_1.next != pointer_2:
            pointer_2_temp = pointer_2.next
            pointer_1_temp = pointer_1.next
            pointer_1.next = pointer_2
            pointer_2.next = pointer_1_temp
            pointer_2 = pointer_2_temp
            pointer_1 = pointer_1_temp



