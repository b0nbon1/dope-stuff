# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep count of the characters 
        count = {}
        # keep maximum characters after replacement
        res = 0
        # left pointer of the window
        l = 0
        # max frequency of the character in our map
        maxf = 0
        # loop through the string and also use r as right pointer window
        for r in range(len(s)):
            # increment the count of the current character in the map
            count[s[r]] = 1 + count.get(s[r], 0)
            # check if the the current current become the maxf and store how many they're
            maxf = max(maxf, count[s[r]])
            # size of the window
            sizeWindow = r - l + 1
            # before opt: if window is not valid, shift left pointer. to check validity use the size of the window minus the max frequent value
            # while sizeWindow - max(count.values()) > k:
            #   count[s[l]] -= 1
            #   l += 1
            while sizeWindow - maxf > k:
                count[s[l]] -= 1
                l += 1
            # compare size of the window with the current maximum substring length
            res = max(res, sizeWindow)
        return res