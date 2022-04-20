def search(nums, target):
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high)//2
    if target == nums[mid]:
      return mid
    if nums[low] <= nums[mid] or target < nums[low]:
      if target > nums[mid]:
        low = mid + 1
      else:
        high = mid - 1
    else:
      if target < nums[mid] or target > nums[high]:
        high = mid - 1
      else:
        low = mid + 1

  return -1

print(search([10,11,1,2,3,4], 11))
