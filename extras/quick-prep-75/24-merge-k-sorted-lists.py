# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# check problem number 20 on this folder for more explaination
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(self.mergeList(l1,l2))
            lists = mergedList
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr1 = l1
        curr2 = l2
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