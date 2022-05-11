# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr1 = list1
        curr2 = list2
        newList = dummy
        while curr1 or curr2:
          if curr1 is None:
            newList.next = curr2
            break
          elif curr2 is None:
            newList.next = curr1
            break
          elif curr1.val == curr2.val:
            newList.next = ListNode(curr1.val)
            newList.next.next = ListNode(curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
            newList = newList.next.next
          elif curr1.val < curr2.val:
            newList.next = ListNode(curr1.val)
            curr1 = curr1.next
            newList = newList.next
          else:
            newList.next = ListNode(curr2.val)
            curr2 = curr2.next
            newList = newList.next
        return dummy.next
            