# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we'll have 2 pointers. left and right one
        l, r = 0, len(s) - 1
        # while both pointers haven't passed each we loop
        while l < r:
            # check the char in position l if is alphanumeric, if not, increment l
            while l < r and not s[l].isalnum():
                l += 1
            # check the char in position r if is alphanumeric, if not, increment r
            while l < r and not s[r].isalnum():
                r -= 1
            # if l char and r char are not similar break out the loop and return not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            # otherwise increment both r and l pointers
            l += 1
            r -= 1
        # the string is palindrome
        return True

