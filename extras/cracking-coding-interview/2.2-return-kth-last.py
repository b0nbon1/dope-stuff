# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# do we know the number of elements?
# follow-up questions -> are we count null as the item or the next item after null
def removeNthFromEnd(head, n):
    fast = slow = head
    for _ in range(n):
        if not fast:
          return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    print(slow.val)
    return head

def removeNthFromEnd2(head, n):
    if head == None:
      return 0
    index = removeNthFromEnd2(head.next, n) + 1
    if index == n:
      print(head.val)
    return index

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
F = ListNode(5)

D.next = F
C.next = D
B.next = C
A.next = B

removeNthFromEnd(A, 1)
