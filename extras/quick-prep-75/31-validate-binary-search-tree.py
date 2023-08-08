# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        # declare a validate func with left and right boundaries that is recursive
        def valid(node, left, right):
            # this our base case
            if not node:
                return True
            # if curr node is greater than our left boundary or less than our right boundary, that is not a bst
            if not (node.val > left and node.val < right):
                return False
            # when moving to the left child we will leave the left boundary as it cause we're going to the lowe elements but our right boundary is not supposed to exceed the parent and vice verse true for the right child
            return (valid(node.left, left, node.val) 
                    and valid(node.right, node.val, right))
        # call the valid func using left bounds as -infinity and right as infinity with the root
        return valid(root, float("-inf"), float("inf"))
