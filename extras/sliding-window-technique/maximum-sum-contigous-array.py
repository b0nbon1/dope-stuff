def maximumSumSubarray(arr, k):
    if len(arr) < k:
        return 0
    maxSum = float("-inf")
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]
        if i >= k:
            currSum -= arr[i-k]
        maxSum = max(maxSum, currSum)
    
    return maxSum

print(maximumSumSubarray([4,2,1,7,8,1,2,8,1,0], 3))