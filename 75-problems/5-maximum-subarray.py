class Solution:
    def maxSubArray(self, nums):
        maxi = nums[0]
        sum = 0
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            maxi = max(sum, maxi)
        return maxi
        