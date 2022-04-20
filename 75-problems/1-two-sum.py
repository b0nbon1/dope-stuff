class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store:
                return [store[diff], i]
            else:
                store[nums[i]] = i