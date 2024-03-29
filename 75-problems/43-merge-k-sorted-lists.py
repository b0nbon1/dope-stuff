from Queue import PriorityQueue
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode()
        tail = dummy
        tail.next = lists[0]
        for l in lists[1:]:
          print("--->")
          curr = l
          tail = tail.next
          while curr and tail:
            if curr.val <=  tail.val:
              print("===>", curr.val, tail.val)
              newNode = ListNode(curr.val)
              newNode.next = tail.next
              tail.next = newNode
              curr = curr.next
            else:
              print("xxxx>", curr.val, tail.val)
            tail = tail.next
          if curr:
            tail.next = curr
        return dummy.next

class Solution2:
  def mergeKLists(self, lists):
    if not lists or len(lists) == 0:
      return None
    while len(lists) > 1:
      mergedList = []
      for i in range(0, len(lists), 2):
        l1 = lists[i]
        l2 = lists[i + 1] if (i+1) < len(lists) else None
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

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        pq = PriorityQueue()
        for node in lists:
            if node:
              pq.put((node.val,node))
        while pq.qsize()>0:
            curr.next = pq.get()[1]
            curr=curr.next
            if curr.next: pq.put((curr.next.val, curr.next))
        return dummy.next



k = ListNode(1)
k.next = ListNode(4)
k.next.next = ListNode(5)

l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(4)

sol = Solution2()
ans = sol.mergeKLists([k,l])

while ans:
  print(ans.val)
  ans = ans.next