def missingNumber(nums):
  sumTotal = 0
  for i in range(len(nums)+1):
    sumTotal += i
  
  sumMissing = 0
  for i in nums:
    sumMissing += i
  
  return sumTotal - sumMissing

def missingNumber1(nums):
  res = 0
  for i in range(len(nums)):
    res += (i - nums[i])
  return res

def missingNumber2(nums):
  res = len(nums)
  for i in range(len(nums)):
    res ^= i ^ nums[i]
  return res

print(missingNumber2([9,6,4,2,3,5,7,0,1]))

# Gauss Summation
# n(n+1)/2