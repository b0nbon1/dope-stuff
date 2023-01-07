# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min should be first element, just incase no elements
        res = float('inf')
        l = 0
        r = len(nums)-1
        # do a binary search the minimum
        while l < r:
          # if the first
          if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
          # get the pivot of the current array
          mid = (r+l)//2
          # compare and replace minimum value with pivot if lower
          res = min(res, nums[mid])
          # check if our mid is on the lower bound or upper bound and update the pointers accordingly
          if nums[mid] > nums[r]:
            l = mid+1
          else:
            r = mid-1
        return min(res,nums[l])
        
