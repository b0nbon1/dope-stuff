class Solution:
    """
        we're going to create subproblem by making the current char as the center then loop going outwards while checking if the created string is palindrome
        Having two pointers and growing them outwards will do the work of checking if they're palindrome
    """
    def longestPalindrome(self, s: str) -> str:
        # store the result string here
        result = [""]
        # the length to use for comparing the string
        resLen = [0]
        for i in range(len(s)):
            # make the current as the centre of our palindrome and then loop going outwards
            # odd length
            l,r = i, i
            self.helper(l, r, s, resLen, result)
            
            # even length
            l,r = i, i+1
            self.helper(l, r, s, resLen, result)
        return result[0]

    def helper(self, l, r, s, resLen, result):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > resLen[0]:
                result[0] = s[l:r+1]
                resLen[0] = r - l + 1
            l -= 1
            r += 1