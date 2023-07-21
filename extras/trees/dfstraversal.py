class Node:
  def __init__(self, val) -> None:
      self.val = val
      self.left = None
      self.right = None


def depthFirstValues(root):
  if not root:
    return []
  stack = [ root ]
  result = []
  while stack:
    current = stack.pop()
    result.append(current.val)
    if current.right: stack.append(current.right)
    if current.left: stack.append(current.left)
  return result

def depthFirstValuesRecurse(root):
  if not root: return []
  leftValues = depthFirstValuesRecurse(root.left)
  rightValue = depthFirstValuesRecurse(root.right)
  return [ root.val ] + leftValues + rightValue


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

print(depthFirstValues(a)); 