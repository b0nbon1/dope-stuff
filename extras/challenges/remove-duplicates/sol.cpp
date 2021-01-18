#include <bits/stdc++.h>

using namespace std;

int removeDuplicates(vector<int> &nums)
{
  int counter = 0;
  for (int i = 1; i < nums.size(); ++i)
  {
    if (nums[i] == nums[i - 1])
    {
      ++counter;
    }
    else
    {
      nums[i - counter] = nums[i];
    }
  }
  return (nums.size() - counter);
}