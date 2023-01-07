# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialise the binary pointers
        l, r = 0, len(nums) - 1
        # do a binary search
        while l <= r:
            # get the pivot of the array
            mid = (l + r) // 2
            # if found return true
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[mid] >= nums[l]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                  l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                  r = mid - 1
                else:
                    l = mid + 1
        return -1