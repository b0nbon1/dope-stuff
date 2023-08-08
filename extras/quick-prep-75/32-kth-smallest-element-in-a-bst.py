# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root
        n = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right

class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # create a stack to store the nodes
        stack = []
        # start at the root of the tree
        current = root
        
        # loop until we have processed all nodes and found the kth smallest value
        while True:
            # traverse as far left as possible from the current node, adding each node to the stack
            while current is not None:
                stack.append(current)
                current = current.left
            
            # if the stack is empty, we have processed all nodes and can exit the loop
            if not stack:
                break
                
            # pop the top node off the stack (which is the next smallest node) and decrement k
            node = stack.pop()
            k -= 1
            
            # if k is 0, we have found the kth smallest value and can return it
            if k == 0:
                return node.val
            
            # set the current node to the right child of the node we just processed
            current = node.right
        
            