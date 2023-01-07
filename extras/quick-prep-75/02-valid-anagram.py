# https://leetcode.com/problems/valid-anagram/

# time: nlogn
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)

# time: O(n) space: O(n)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if length is same, if not return false
        if len(s) != len(t):
            return False
        # hashMaps to store the count of the characters
        countS, countT = {}, {}

        # iterate through the s and t and add character as keys and number of appearance as values
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # compare both dict if looks the same
        return countS == countT