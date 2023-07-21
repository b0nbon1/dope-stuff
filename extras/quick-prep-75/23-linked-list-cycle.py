# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hash set to store the nodes
        unique_nodes = set()
        curr = head
        # iterate through the list
        while curr:
            # check if next node is in the set
            if curr.next in unique_nodes:
                return True
            # if not add curr node
            unique_nodes.add(curr)
            curr = curr.next
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # have slow pointer and fast pointer
        # we will use the fast pointer to catchup with th slow pointer if there is a cycle or exit the iteration if there is not
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if fast has catchup we return true
            if slow == fast:
                return True
        return False