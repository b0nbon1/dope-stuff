function smallestSumSubarray(target: number, array: number[]): number {
  let minWindowSize = 0;
  let currentWindowSum = 0;
  let windowStart = 0;
  for(let windowEnd = 0; windowEnd < array.length; windowEnd++) {
    currentWindowSum += array[windowEnd];

    while(currentWindowSum >= target) {
      minWindowSize = Math.min(minWindowSize, windowEnd - windowStart + 1);
      currentWindowSum -= array[windowStart];
      windowStart++;
    }
  }
  return minWindowSize;
}