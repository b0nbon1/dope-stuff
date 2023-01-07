# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # have two pointers left as the slow pointer and r as the fast pointer
        l = 0
        # loop through the days and start at the second day
        for r in range(1, len(prices)):
            # compare prices of the left&right pointer and if right is less than left, update left to be at right
            if prices[r] < prices[l]:
                l = r
            # check maximum profit made and store it
            res = max(res, prices[r] - prices[l])
        return res