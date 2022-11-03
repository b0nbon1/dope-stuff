# follow-up questions
# does it have duplicates or not?
# is the left side less than or right side less than the left
# if duplicates should it go to the left or right?
class BST:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# def validateBst(tree, min= float("-inf"), max=float("inf")):
#   if tree is None:
#     return True
#   else:
#     if tree.value <= min or tree.value > max:
#       return False
#     return validateBst(tree.right, tree.value, max) and validateBst(tree.left, min, tree.value)

def validateBst(tree, left = float("-inf"), right = float("inf")):
  if not tree:
    return True
  # check validity of current tree
  if not (tree.val <= right and tree.val > left):
    return False
  # we check the left tree updating the right bound and the right tree updating the left bound with current node and keep the right
  return validateBst(tree.left, left, tree.val) and validateBst(tree.right, tree.val, right)


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(6)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
print(validateBst(root))
