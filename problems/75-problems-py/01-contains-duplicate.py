def containsDuplicate(nums):
    duplicates_set = set()
    for x in nums:
        if x in duplicates_set:
            return True
        duplicates_set.add(x)
    return False