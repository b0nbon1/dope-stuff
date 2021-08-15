// sliding window algorithm
function lengthOfLongestSubstring(s: string): number {
  if(s === null || s.length === 0) return 0;
  let i = 0;
  let j = 0;
  let max = 0;
  const set = new Set();
  while(i < s.length) {
      while(set.has(s[i])) {
          set.delete(s[j]);
          ++j;
      }
      set.add(s[i]);

      max = Math.max(max, i-j+1)
      ++i;
  }
  return max;
};
