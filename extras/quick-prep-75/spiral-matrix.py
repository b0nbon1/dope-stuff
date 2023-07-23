class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # initialiaze the left and right pointers
        l, r = 0, len(matrix[0])
        # initialiaze the top and bottom pointers
        top, bottom = 0, len(matrix)
        result = []
        # loop through the matrix and make sure the pointers are within the boundaries
        while l < r and top < bottom:
            # start with the top row, from left to right while appending the items to a list
            for i in range(l, r):
                result.append(matrix[top][i])
            # increment the top row to top + i since you don't want to go back there
            top += 1
            # go the furthest right column while at it read the elements from top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][r-1])
            # shrink in the right column to right - i
            r -= 1
            # to catch an edge where you had only one row, you have to check, if true break out
            if not (l < r and top < bottom):
                break
            # go to the most bottom row, loop through from right to left
            # remember our right pointer is at last index + 1 so we have to decrement and loop reverse
            for i in range(r-1, l-1, -1):
                result.append(matrix[bottom - 1][i])
            # shrink the bottom to bottom - 1
            bottom -= 1
            # go to the most left col, loop through from bottom to top
            # remember our bottom pointer is at last index + 1 so we have to decrement and loop reverse
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][l])
            # decrement the left pointer
            left -= 1
            # repeat this since you'll be moving inwards until our case is not true
        return result
