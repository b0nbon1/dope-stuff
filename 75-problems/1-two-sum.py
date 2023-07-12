class Solution:
    def twoSum(self, nums, target):
        # store the differences
        store = {}
        # go through the nums
        for i in range(len(nums)):
            # get the difference of the num and the target
            diff = target - nums[i]
            # check if the difference exists in the store
            if diff in store:
                # if exists return the sum number and the current num positions
                return [store[diff], i]
            else:
                # if diff doesn't exists, store the current num
                store[nums[i]] = i
                