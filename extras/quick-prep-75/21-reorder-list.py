# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # have slow and fast pointer, the slow pointer will be moving slow and fast pointer will be jumping to position ahead
        # to find the middle of the list
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast  = fast.next.next
        
        # reverse the second half here
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two halves, kinda like zipping
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2