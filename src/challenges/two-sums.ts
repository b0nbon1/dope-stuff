function twoSum(nums: number[], target: number): number[] {
  const pair = [0,0];
  let sum = 0;
  let solution = 0;
  for(let i = 0; i < nums.length; i++) {
      for(let j = 0; j < nums.length; j++){
          if(j === i) continue;
          sum = nums[i] + nums[j];
          if(sum === target) {
              pair[0] = i;
              pair[1] = j;
              solution = sum;
              break;
          }
      }
      if(solution == target) break;
  }
  return pair;
};

// faster solution 
function twoSum1(nums: number[], target: number): number[] {
  const diff = {};
  let pair = [0, 0];
  for(let i = 0; i < nums.length; i++) {
    if (diff[target - nums[i]] !== undefined) {
      pair = [diff[target - nums[i]], i];
      break;
    } else {
      diff[nums[i]] = i;
    }
  }
  return pair;
};

