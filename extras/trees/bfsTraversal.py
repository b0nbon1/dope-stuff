class Node:
  def __init__(self, val) -> None:
      self.val = val
      self.left = None
      self.right = None

def bfsTraversal(tree):
  if not tree: return []

  queue = [tree]
  result = []
  while queue:
    current = queue.pop(0)
    result.append(current.val)
    if current.left: queue.append(current.left)
    if current.right: queue.append(current.right)
  return result


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(bfsTraversal(a)); 

