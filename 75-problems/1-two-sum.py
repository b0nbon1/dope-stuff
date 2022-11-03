class Solution:
    def twoSum(self, nums, target):
        store = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store:
                return [store[diff], i]
            else:
                store[nums[i]] = i
                