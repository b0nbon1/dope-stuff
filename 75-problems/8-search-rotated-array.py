def search(nums, target):
  low = 0
  high = len(nums) - 1
  while low <= high:
    mid = low + (high-low)//2
    if target == nums[mid]:
      return mid
    # left sorted portion
    if nums[mid] >= nums[low]:
      if target > nums[mid] or target < nums[low]:
        low = mid + 1
      else:
        high = mid - 1
    # right sorted portion
    else:
      if target < nums[mid] or target > nums[high]:
        high = mid - 1
      else:
        low = mid + 1
  

  return -1

print(search([5,6,7,8,10,11,1,2,3,4], 11))
