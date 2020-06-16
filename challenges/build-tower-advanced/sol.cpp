#include <vector>
#include <string>
#include <iostream>

std::vector<std::string> towerBuilder(int nFloors, std::vector<int> nBlockSz)
{
  int last_floor = nFloors * nBlockSz[0] * 2 - nBlockSz[0];
  std::vector<std::string> tower;
  int floor = 0;
  for(int i = 0; i < nFloors * nBlockSz[1]; i++)
  {
    if(i % nBlockSz[1] == 0) floor += 1;
    int width = floor * nBlockSz[0] * 2 - nBlockSz[0];
    int spaceWidth = (last_floor - width)/2;
    tower.push_back(std::string(spaceWidth, ' ') + std::string(width, '*') + std::string(spaceWidth, ' '));
  }

  return tower;
}

int main()
{
 std::vector<std::string> built = towerBuilder(3, {4,2});
  for(std::string x : built) {
    std::cout << x << std::endl;
  }
}
