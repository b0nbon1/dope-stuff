# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      # have a slow and fast pointer
        slow = fast = head
        # fast forward the fast pointer to match the length from nth
        for _ in range(n):
            fast = fast.next
        # if not fast means it went to null, the we can just remove the first element
        if not fast:
            return head.next
        # while fast we can keep moving both pointers forward until fast is at the end, slow one will be at the position we need it to be at
        while fast.next:
            slow = slow.next
            fast = fast.next
        # we can remove the node that we will be at
        slow.next = slow.next.next
        return head