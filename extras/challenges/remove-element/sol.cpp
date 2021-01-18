#include <bits/stdc++.h>

using namespace std;

int removeElement(vector<int> &nums, int val)
{
  int counter = 0;
  for (int i = 0; i < nums.size(); ++i)
  {
    if (nums[i] == val)
    {
      ++counter;
    }
  }
  return (nums.size() - counter);
}

int removeElemen(vector<int> &nums, int val)
{
  for (int i = 0; i < nums.size(); i++)
    if (nums[i] == val)
      nums.erase(nums.begin() + i--);
  return nums.size();
}

int removeEleme(vector<int> &nums, int val)
{

  sort(nums.begin(), nums.end());
  vector<int>::iterator new_end;
  new_end = remove(nums.begin(), nums.end(), val);

  nums.erase(new_end, nums.end());

  return nums.size();
}
