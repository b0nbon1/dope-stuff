class Node:
  def __init__(self, val) -> None:
      self.val = val
      self.left = None
      self.right = None

def treeSum(root):
  if not root: return 0
  return treeSum(root.right) + treeSum(root.left) + root.val

def treeSumBfs(root):
  if not root: return 0
  queue = [root]
  result = 0
  while queue:
    current = queue.pop(0)
    result += current.val
    if current.left: queue.append(current.left)
    if current.right: queue.append(current.right)
  return result


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(treeSumBfs(a)) # -> 21
