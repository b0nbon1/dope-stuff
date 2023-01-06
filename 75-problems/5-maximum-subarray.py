class Solution:
    def maxSubArray(self, nums):
        maxi = nums[0]
        sum = 0
        for n in nums:
            print(n)
            if sum < 0:
                sum = 0
            sum += n
            maxi = max(sum, maxi)
        return maxi

sol = Solution()

sol.maxSubArray([4,-1,5,-10,4,6,7])
        