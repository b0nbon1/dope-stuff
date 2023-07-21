# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
		# t O(n) M O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if node is null, break
        if not head:
          return None
        # initialise the prev_node to store the reversed list and curr_node to keep track of the curr_node
        curr_node, prev_node = head, None
        # reverse the list using iteration
        while curr_node:
          # store the next node in temp space since we will be replacing it
          temp = curr_node.next
          # change the point from pointing next to the previous node
          curr_node.next = prev_node
          # update out previous node with the curr_node which has the reverse list
          prev_node = curr_node
          # update the iteration node with the next node
          curr_node = temp
        return prev_node