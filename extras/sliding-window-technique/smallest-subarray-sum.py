def smallestSubarraySum(arr, sum):
    minWindowSize = float('inf')
    l = 0
    currSum = 0
    for r in range(len(arr)):
        currSum += arr[r]
        while currSum >= sum:
            minWindowSize = min(minWindowSize, r-l+1)
            currSum -= arr[l]
            l += 1
    return minWindowSize

print(smallestSubarraySum([4,2,2,7,8,1,2,8,10], 8))
        
            
                
            
