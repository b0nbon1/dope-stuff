#include <iostream>
#include <vector>
#include <map>

typedef std::map <int, int> MAP;

auto findel(MAP &map, const int &findMe) {
    try {
        const int& value = map.at(findMe);
        return value;
    }
    catch (const std::out_of_range&) {
        map[findMe]++;
        return map.at(findMe);
    }
}
 

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
  MAP store;
  for(int i = 0; i < arr.size(); i++)
  {
    if (findel(store, arr[i]) > n)
    {
      arr.erase(arr.begin() + i);
      continue;
    }
    store[arr[i]]++;
  }
  return arr;
}

int main()
{
  std::vector<int> del = deleteNth({1, 2, 3, 1, 1, 2, 2, 3, 3, 2, 4, 5, 1}, 5);
  for(auto i : del) 
  {
    std::cout << "Value: " << i << std::endl;
  }
  return 0;
}