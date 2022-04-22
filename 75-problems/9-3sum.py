def threeSum(nums):
  res = []
  nums.sort()
  for i, x in enumerate(nums):
    if i > 0 and x == nums[i - 1]:
      continue

    l, r = i + 1, len(nums) - 1
    while l < r:
      threeS = x + nums[l] + nums[r]
      if threeS > 0:
        r -= 1
      elif threeS < 0:
        l += 1
      else:
        res.append([x, nums[l], nums[r]])
        l += 1
        while nums[l] == nums[l - 1] and l < r:
          l += 1
  return res
