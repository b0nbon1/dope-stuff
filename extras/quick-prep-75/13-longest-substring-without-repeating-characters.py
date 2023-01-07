# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to store the current running longest substring
        charSet = set()
        # l pointer for the left side of the window
        l = 0
        # store the longest maximum length of the substring
        res = 0
        # loop through the array, r will represent the right pointer of the window
        for r in range(len(s)):
            # check if the current character is already in the set
            while s[r] in charSet:
                # if already the keep remove characters in the set until the duplicate is remove
                charSet.remove(s[l])
                # increment the left point
                l += 1
            # otherwise add the character to the set
            charSet.add(s[r])
            # find the maximum length
            res = max(res, r - l + 1)
        return res