class Node:
  def __init__(self, val) -> None:
      self.val = val
      self.left = None
      self.right = None

def treeMinValue(root):
  if not root: return float("inf")
  return min(root.val, treeMinValue(root.right), treeMinValue(root.left))



a = Node(3);
b = Node(11);
c = Node(4);
d = Node(4);
e = Node(-2);
f = Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(treeMinValue(a)) # -> -2