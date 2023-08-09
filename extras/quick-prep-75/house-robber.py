class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 and rob2 will cache the results, where both will be used to store the max of the alternetive robbed houses
        rob1, rob2 = 0,0
        for n in nums:
            rob1, rob2 = rob2, max(n+rob1, rob2)
        return rob2