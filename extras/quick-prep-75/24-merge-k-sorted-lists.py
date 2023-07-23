# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# check problem number 20 on this folder for more explaination
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # check if there are lists, otherwise return null
        if not lists:
            return None
        # while our lists are more than one keep merging them
        while len(lists) > 1:
            # create a merge list for the array
            mergedList = []
            # loop through skipping twice since we are merging two lists
            for i in range(0, len(lists), 2):
                # list 1 will be at the first index
                l1 = lists[i]
                # list 2 will be in the next index from l1 as long as index not out of bounds otherwise will be null
                l2 = lists[i+1] if (i+1) < len(lists) else None
                # take a l1 and l2 merge 
                twoMergedLists = self.mergeList(l1,l2)
                # after merging, append them to the last index
                mergedList.append(twoMergedLists)
            # once finished the first round the list will be half of the main since we have merged two lists 
            # we will make mergedList to be lists and repeat the process untill we remain with one element on the list
            lists = mergedList
        # return the first index which will have our merged element
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