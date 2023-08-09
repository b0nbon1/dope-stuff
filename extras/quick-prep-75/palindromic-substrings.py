class Solution:
    def countSubstrings(self, s: str) -> int:
        # number of the palindromic substrings
        res = [0]
        for i in range(len(s)):
            # make the current as the centre of our palindrome and then loop going outwards
            # odd length, get alll odd strings
            l,r = i, i
            self.helper(l, r, s, res)
            
            # even length
            l,r = i, i+1
            self.helper(l, r, s, res)
        return res[0]

    def helper(self, l, r, s, res):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res[0] += 1
            l -= 1
            r += 1