# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board, word):
        # define the rows and cols
        cols, rows = len(board), len(board[0])
        # create path that will be used to mark the passed rows
        path = set()

        # our dfs take sthe row and col and also the index of the word
        def dfs(col,row, i):
            # if length word is equal to the index of word return true
            if i == len(word):
                return True

            # check the boundaries and the cases -> must be with the board, not exist in path set, word is equal to the current word index
            if (
                col < 0
                or col > cols - 1
                or row < 0
                or row > rows - 1
                or board[col][row] != word[i]
                or (col, row) in path
            ):
                return False
            # if cases pass add the square to the path
            path.add((col, row))
            # go through all the possiblities in the all sides of the current square
            res = dfs(col, row-1, i+1) or dfs(col, row+1, i+1) or dfs(col+1, row, i+1) or dfs(col-1, row, i+1)
            # after you found a path or not, remove the path from the set to avoid false cases
            path.remove((col, row))
            # return True or False when word found or not
            return res
    
        # loop through the board
        for c in range(cols):
            for r in range(rows):
                # if the dfs returns true means the wor exists return True otherwise continue
                if dfs(c, r, 0):
                    return True

        return False
