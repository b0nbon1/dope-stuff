# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # stores the longest_streak of number
        longest_seq = 0
        # convert our nums array into set for O(1) checking if elemenet exists
        set_nums = set(nums)
        # loop through all of the nums
        for n in nums:
            # current streak
            curr_seq = 1
            # store copy of current number to avoid increment of for loop
            curr_num = n
            # checks if there is number less than it to avoid looping twice, eg. 3,2,1 we not loop through 3 and 2
            if (curr_num - 1) not in set_nums:
                # checks the next number in the loop, eg. 1 next number is 2
                while curr_num + 1 in set_nums:
                    curr_num += 1
                    curr_seq += 1
                # checks and stores the longest streak
                longest_seq = max(curr_seq, longest_seq)
        return longest_seq
    