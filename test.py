import unittest

def minHeightBst(array):
        mid = len(array)//2
        bst = BST(array[mid])
        buildTree(array, bst, 0, mid-1)
        buildTree(array, bst, mid+1, len(array)-1)
        return bst

def buildTree(array, bst=None, startIdx=0, endIdx=0):
    if startIdx > endIdx or startIdx<0 or endIdx>len(array)-1:
        return None
    mid = (endIdx + startIdx)//2
    print("--->", mid)
    bst.insert(array[mid])
    buildTree(array, bst, startIdx, mid-1)
    buildTree(array, bst, mid+1, endIdx)
    

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)



array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
tree = minHeightBst(array)

validateBst(tree)
print(getTreeHeight(tree))

inOrder = inOrderTraverse(tree, [])

print(inOrder)

