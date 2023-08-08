class TrieNode: 
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        # iterate through the root node
        curr = self.root
        for c in word:
            # check if the word exists in children, if not add it to the children
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # if exists, go to the child
            curr = curr.children[c]
        # repeat until end of the word, then mark it as word
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            # iterate through the word
            for i in range(j, len(word)):
                c = word[i]
                # if word is ., means it's a wild card so we have to dfs through the it
                if c == ".":
                    # check through all the children 
                    for child in curr.children.values():
                        # recurse through the children
                        if dfs(i+1, child):
                            return True
                    return False
                # word not ., check if it matches with trie
                else:
                    # if not break out otherwise continue with iteration
                    if c not in curr.children:
                        return False
                    # go to the next child if char exists
                    curr = curr.children[c]
            # check if current created word is an existing word
            return curr.word
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)