# https://leetcode.com/problems/3sum/


class Solution:
    # time: O(nlogn) + O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the input array
        nums.sort()
        # loop through the nums
        for i, a in enumerate(nums):
            # compare the nums, and ignore the duplicates when picking the first number
            if i > 0 and a == nums[i - 1]:
                continue
            # since we already have the first number stored in a, we can use 2sum II to find the second and third
            # we will have the right pointer and left pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                # get the current 3sum
                threeSum = a + nums[l] + nums[r]
                # if sum greater than zero, shift the right pointer
                if threeSum > 0:
                    r -= 1
                # if sum smaller than zero, shift the left pointer
                elif threeSum < 0:
                    l += 1
                # if sum is equal to zero, we have our answer now
                else:
                    # append the nums to the result array
                    res.append([a, nums[l], nums[r]])
                    # increment left pointer
                    l += 1
                    # and if left pointer is equal to left point + 1, increment it to avoid duplicates in our results
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
