# palindrome defination
# what output should we expect out of it
# 

def isPalindrome(head):
  slow = fast  = head
  while fast != None and fast.next != None:
    fast = fast.next.next
    slow = slow.next
  if fast != None: # odd nodes: let right half smaller
    slow = slow.next
  
  slow = reverse(slow)
  fast = head
  while slow != None:
    if fast.val != slow.val:
      return False
    fast = fast.next
    slow = slow.next
  return True

def reverse(node):
  prev = None
  while node != None:
    next = node.next
    node.next = prev
    prev = node
    node = next
  return prev

# https://mfsafrica.zoom.us/j/85231833116?pwd=VTB0eWp3aXovbHB5bko1cWg4RHB6UT09