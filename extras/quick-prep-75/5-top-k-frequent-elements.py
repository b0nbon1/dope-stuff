# https://leetcode.com/problems/top-k-frequent-elements/

# bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map to store the count the occurances of a number
        count = collections.defaultdict(int)
        # iterate through and store the  occurances
        for n in nums:
            count[n] += 1
        # create a buckets for the items and we know an item can occur maximum of len(nums) times so each bucket will take the values that occur the index times of the bucket
        # eg. 1,1,2,2,3,3,3 -> we have 7 items so 7 buckets bucket 0-1 will have nothing, bucket 2 will carry 1 and bucket 3 will carry 3, and the rest will be empty
        buckets = [[] for i in range(len(nums)+1)]
        # add items to their respective buckets as explained
        for key, value in count.items():
            buckets[value].append(key)
        result = []
        # since the most occur numbers are on the higher indexes of our buckets we will start iterating from right going left
        for i in range(len(buckets)-1, -1, -1):
            # if bucket not empty
            if len(buckets[i]) > 0:
                # go through each item in a bucket
                for n in buckets[i]:
                    # append the top k into the result
                    result.append(n)
                    # if length equal to k, break out and return the result array.
                    if len(result) == k:
                        return result
        return []
