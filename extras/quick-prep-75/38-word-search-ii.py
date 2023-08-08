# https://leetcode.com/problems/word-search-ii/

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0
    
    def insert(self, word: str) -> None:
        # iterate through the root node
        curr = self
        curr.refs += 1
        for c in word:
            # check if the word exists in children, if not add it to the children
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # if exists, go to the child
            curr = curr.children[c]
            curr.refs += 1
        # repeat until end of the word, then mark it as word
        curr.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # create a trie for the given words
        for w in words:
            root.insert(w)
        # know the cols and rows for the board
        ROWS, COLS = len(board), len(board[0])
        # have a sets for the results and also avoid duplicates marking the visited
        res, visit = set(), set()

        direction = [
                      [-1, 0],
                      [1, 0],
                      [0,-1],
                      [0,1],
                    ]

        def dfs(r,c, node, word):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or  (r,c) in visit
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)
            for i in range(len(direction)):
                x, y = direction[i][0], direction[i][1]
                dfs(r+x, c+y, node, word)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
        return list(res)