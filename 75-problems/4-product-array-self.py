class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodArr = [1] * (len(nums))
        pre = 1
        for i in range(len(nums)):
            prodArr[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            prodArr[i] *= post
            post *= nums[i]
        
        return prodArr