# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # store the unique numbers in set
        hashset = set()

        for n in nums:
            # iterate and check if the number is in the set, if not add to the set.
            if n in hashset:
                # if exists retturn true
                return True
            hashset.add(n)
        # if doesn't have duplicates, return false
        return False