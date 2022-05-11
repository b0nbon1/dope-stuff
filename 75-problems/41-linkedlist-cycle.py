# hashmaps use below
def hasCycle(head):
  hshset = set()
  curr = head
  while curr:
    if curr in hshset:
      return True
    hshset.add(curr)
    curr = curr.next
  return False

# Floyd's Tortoise & Hare
def hasCycle(head):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False