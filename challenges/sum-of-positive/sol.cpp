#include <vector>
#include <iostream>

int positive_sum (const std::vector<int>& arr){
  int sum = 0;

  for(int i : arr)
    if(i >= 0) sum += i;
  return sum;
}

int main() 
{
  std::cout << positive_sum({1,-4,7,12});
}

