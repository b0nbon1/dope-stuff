# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # since our output list can't be empty, create a dummy node
        dummy = ListNode()
        # assign dummy node to our newList pointer
        newList = dummy
        while list1 or list2:
          # if our list is empty, append list 2 and break
          if list1 is None:
            newList.next = list2
            break
          # same as here
          if list2 is None:
            newList.next = list1
            break
          # if both head values are same, append both to our output list
          if list1.val == list2.val:
            newList.next = ListNode(list1.val)
            newList.next.next = ListNode(list2.val)
            list1 = list1.next
            list2 = list2.next
            newList = newList.next.next
          # if list1 head val is less than list2, append it to output
          elif list1.val < list2.val:
            newList.next = ListNode(list1.val)
            list1 = list1.next
            newList = newList.next
          # if list2 head val is less than list1, append it to output
          else:
            newList.next = ListNode(list2.val)
            list2 = list2.next
            newList = newList.next
        return dummy.next