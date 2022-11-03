'''
nums -> |1 | 2| 4|7|
pre ->  |1 | 1| 2|8|
post -> |56|28|14|8|
prod -> |56|28|14|8|
'''

# [1,2,4,7]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,1,1,1,1]
        prodArr = [1] * (len(nums))
        # 1 [1,1,1,1,1]
        pre = 1
        for i in range(len(nums)):
            prodArr[i] = pre
            pre *= nums[i]
        # [1,1, 2, 8, 56]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            prodArr[i] *= post
            post *= nums[i]
        
        return prodArr

        [56, 56]