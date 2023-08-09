class Solution:
    def rob(self, nums: List[int]) -> int:
        # if it's just one house rob only that one
        if len(nums) == 1:
            return nums[0]
        # rob the house without the first and also without the last again and then check which one is the highest
        return max(self.heperRob(nums[1:]), self.heperRob(nums[:-1]))
    
    # refer to houser robber problem
    def heperRob(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n+rob1, rob2)
        return rob2