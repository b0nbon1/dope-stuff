import collections

def topKFrequent(nums, k):
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        buckets = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            buckets[value].append(key)
        result = []
        print(buckets)
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) > 0:
                for n in buckets[i]:
                    result.append(n)
                    if len(result) == k:
                        return result
        return []

print(topKFrequent([1,1,5,5,5,3,2,3,1,4,4,6,6], 2))