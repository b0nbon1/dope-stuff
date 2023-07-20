def twoSum(nums, target):
    difference_map = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in difference_map:
            return [difference_map[difference], i]
        difference_map[nums[i]] = i
    return [-1,-1]

print(twoSum([2,5,6,8,7,9], 13))