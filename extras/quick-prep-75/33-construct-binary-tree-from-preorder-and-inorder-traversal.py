# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # the preorder will give you the current root value
        root = TreeNode(preorder[0])
        # the inorder, all the values on the left from the root value will be the left subtree
        mid = inorder.index(preorder[0])
        # we can recurse to the left subtree using the values
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root