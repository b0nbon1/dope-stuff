# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # initialise a map with default of list
        ans = collections.defaultdict(list)

        # iterate through the array
        for s in strs:
            # initialise an array to store the 26 characters' count in a letter
            count = [0] * 26
            # iterate through each string while counting the characters
            for c in s:
                count[ord(c) - ord("a")] += 1
            # store the count as tuple and use it as key in our hashmap while append the characher that has similar tuple design
            ans[tuple(count)].append(s)
        # return the values of the map which will have a 2D array that has grouped the anagrams
        return ans.values()