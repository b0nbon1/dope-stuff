class Solution:
    def maxProduct(self, nums):
        maxi = max(nums)
        currentMax, currentMin = 1, 1
        for x in nums:
            if x == 0:
                currentMax, currentMin = 1, 1
                continue
            temp = x * currentMax
            
            currentMax = max(x * currentMax, currentMin * x, x)
            currentMin = min(temp, currentMin * x, x)
            
            maxi = max(currentMax, maxi)
        
        return maxi