def containsDuplicate(self, nums):
  storeSet = set()
  for i, x in enumerate(nums):
      if x in storeSet:
          return True
      else:
          storeSet.add(x)
  return False