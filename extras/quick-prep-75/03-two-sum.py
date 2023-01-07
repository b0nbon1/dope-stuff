# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the previous nums in the hashmap and using the diff from the target
        prevMap = {}  # val -> index
        # iterate through the nums and check diff if is in the map
        for i, n in enumerate(nums):
            # get the current difference
            diff = target - n
            # if diff exists in the map
            if diff in prevMap:
                # that's the difference, return the indexes
                return [prevMap[diff], i]
            # otherwise update the map with the current num and index as value
            prevMap[n] = i