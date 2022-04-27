def reverseList(head):
  prev, curr == None, head
  # T O(n), M O(1)
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev

#[1,2,4, Null]
def reverseList1(head):
  if not head:
    return None
  newHead = head
  if head.next:
    newHead = reverseList1(head.next)
    head.next.next = head
  head.next = None
  return newHead