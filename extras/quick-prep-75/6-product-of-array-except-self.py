# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we're use this as our output store
        result = [1]* len(nums)
        # our prefix will start before the array with one as we move
        pre = 1
        # iterate through the nums while resulting the prefix
        for i in range(len(nums)):
            # put the prev number asin prefix on the current
            result[i] = pre
            # get the new prefix while multiplying with prefix with current num
            pre *= nums[i]
        
        # our postfix will start after the array with as we move backwards
        post = 1
        # iterate from the last
        for i in range(len(nums)-1, -1, -1):
            # to add postfix to our output array, multiply it with the post fix
            result[i] *= post
            # get the next postfix by multiply the current number index from input array
            post *= nums[i]
        
        return result