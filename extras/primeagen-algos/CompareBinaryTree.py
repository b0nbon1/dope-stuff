class TreeNode:
    def __init__(self, value, left= None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def compare(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.value != b.value:
        return False
    return compare(a.left, b.left) and compare(a.right, b.right)

treeA = TreeNode(20)
treeA.left = TreeNode(10)
treeA.right = TreeNode(50)
treeA.left.right = TreeNode(15)
treeA.left.left = TreeNode(5)

treeB = TreeNode(20)
treeB.left = TreeNode(10)
treeB.right = TreeNode(50)
treeB.left.right = TreeNode(15)
treeB.left.left = TreeNode(5)

print(compare(treeA, treeB))