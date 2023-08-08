# implement a trie node,
# children will hold the  child nodes for the root
# endOfWord will mark if we are at the end of theword
class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        # declare root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # iterate through the root node
        curr = self.root
        for c in word:
            # check if the word exists in children, if not add it to the children
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # if exists, go to the child
            curr = curr.children[c]
        # repeat until end of the word, then mark it as word
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        # go through the tree while checking if the word exists
        for c in word:
            # if it doesn't return false
            if c not in curr.children:
                return False
            # else go the next level
            curr = curr.children[c]
        # once done and made sure the word exists, use endOfWord check to determine if it was a word or not
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        # similar to search but we don't need to check for endOfWord since we're just looking for prefix
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)