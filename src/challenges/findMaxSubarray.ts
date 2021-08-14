function findMaxSumSubarray(array: number[], k: number): number {
  let maxVal = 0;
  let currentRunningSum = 0;

  for (let i = 0; i < array.length; i++) {
    currentRunningSum += array[i];
    if(i >= k - 1) {
      maxVal = Math.max(maxVal, currentRunningSum);
      currentRunningSum -= array[i - (k-1)];
    }
  }
  return maxVal;
}