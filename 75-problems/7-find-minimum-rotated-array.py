def findMin(nums):
  low = 0
  high = len(nums)-1
  track = nums[0]
  while low <= high:
    mid = (low+high)//2
    if nums[low] < nums[high]:
      return min(track, nums[low])
    track = min(track, nums[mid])
    if nums[mid] >= nums[low]:
      low = mid + 1
    else:
      high = mid - 1
  return track

print(findMin([3,4,5,1,2]))