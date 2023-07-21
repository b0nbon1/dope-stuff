def reverseList(head):
  prev, curr == None, head
  # T O(n), M O(1)
  # 1 -> 2 -> 3 -> 4
  # null <- 
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
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