import collections

def topKFrequent(nums, k):
        # init a dict to count occurances
        count = collections.defaultdict(int)
        # count the occurances
        for n in nums:
            count[n] += 1
        # create buckets(2-D array) -> assuming the occurances can't go past the length of the array
        buckets = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            # append items into the bucket using the occurance as the index and value in bucket
            buckets[value].append(key)
        result = []
        # traverse through the bucket
        for i in range(len(buckets)-1, -1, -1):
            # if bucket not empty
            if len(buckets[i]) > 0:
                # run through the bucket
                for n in buckets[i]:
                    # append the items in the result
                    result.append(n)
                    # if we have reached the K value -> return the result
                    if len(result) == k:
                        return result
        return []

print(topKFrequent([1,1,5,5,5,3,2,3,1,4,4,6,6], 2))