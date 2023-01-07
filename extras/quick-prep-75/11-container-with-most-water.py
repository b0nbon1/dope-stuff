# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointers, with the lists
        l, r = 0, len(height) - 1
        # record max area here
        res = 0
        # loop through the pointer while going inwards
        while l < r:
            # get the minimum height cause that's where the water can reach, by comparing r and l value pointer
            minHeight = min(height[l], height[r])
            # get the current area
            area =  minHeight * (r - l)
            # get the maximum area by comparing maximum area and current area
            res = max(res, area)
            # if left height is less than right height, move the left height higher
            if height[l] < height[r]:
                l += 1
            # otherwise move right lower
            else:
                r -= 1
        return res