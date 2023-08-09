class Solution:
    def climbStairs(self, n: int) -> int:
        # we'll use dp to solve this one, where one will be used to cache the previous steps and two will be used for the current steps
        # 5 -> 1 step to get to 5
        # 4 -> we can take 1 step to 5
        # 3 -> we can take 1 way + 1 way from 4 -> 2 ways
        # 2 -> we can 2 ways from 3 or 1 way from 4 -> 3 ways
        # 1 -> we can take 3 ways from 2 or 2 ways from 3 -> 5 ways
        # 0 -> we can take 5 ways from 1 or 3 ways from 2 -> 8 ways
        # so as you have noticed we can cache the result from the previous two value and use it get the next ways
        one, two = 1, 1
        for i in range(n-1):
            one, two = two + one, one
        return one
        