import collections

class TreeNode:
    def __init__(self, value, left= None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def bfs(head, needle):
    q = collections.deque([head])
    while q:
        curr = q.popleft()
        if curr.value == needle:
            return True
        if curr.left:
          q.append(curr.left)
        if curr.right:
          q.append(curr.right)
    return False

tree = TreeNode(20)
tree.left = TreeNode(10)
tree.right = TreeNode(50)
tree.left.right = TreeNode(15)
tree.left.left = TreeNode(5)
tree.left.left.right = TreeNode(7)
tree.left.left.left = TreeNode(4)
tree.right.left = TreeNode(30)
tree.left.right.left = TreeNode(45)
tree.left.right.right = TreeNode(55)
tree.right.left.right = TreeNode(29)
tree.right.left.left = TreeNode(32)
tree.right.right = TreeNode(100)
tree.right.right.left = TreeNode(107)
tree.right.right.right = TreeNode(103)

print(bfs(tree, 37))

