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


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty input
        if not nums:
            return 0

        # Initialize a set to store the elements in the input array
        num_set = set(nums)
        max_length = 1

        while num_set:
            # Take an arbitrary element from the set
            num = num_set.pop()

            # Initialize the length of the consecutive sequence starting from this element
            length = 1

            # Check for elements that come before this one
            left = num - 1
            while left in num_set:
                num_set.remove(left)
                left -= 1
                length += 1

            # Check for elements that come after this one
            right = num + 1
            while right in num_set:
                num_set.remove(right)
                right += 1
                length += 1

            # Update the maximum length if necessary
            max_length = max(max_length, length)

        return max_length
