class Node:
  def __init__(self, val) -> None:
      self.val = val
      self.left = None
      self.right = None

def treeIncludes(root, target):
  if not root: return False
  if root.val == target: return True
  return treeIncludes(root.right, target) or treeIncludes(root.left, target)



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

print(treeIncludes(a, 'h'))

