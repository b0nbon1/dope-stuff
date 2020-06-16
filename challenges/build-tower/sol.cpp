#include <vector>
#include <string>
#include <iostream>

 std::string operator*(std::string s, size_t count)
    {
      std::string ret;
      for(size_t i = 0; i < count; ++i)
      {
          ret = ret + s;
      }
      return ret;
    }

class Kata
{  
  public:
    
    std::vector<std::string> towerBuilder(int nFloors)
    {
      std::vector<std::string> tower;
      std::string strk = "*";
      std::string spaced = " ";
      long blocks = nFloors * 2 - 1;
      for(int i = 1; i <= nFloors; i++)
      {
        std::string flr = "";
        size_t num_strk = i*2-1;
        size_t num_space = (blocks - num_strk)/2;
        flr += spaced * num_space;
        flr += strk * num_strk;
        if(i != nFloors) flr += spaced * num_space;
        tower.push_back(flr);
      }
      return tower;
    }
};


int main()
{
  std::string stuff = "*";
  // std::string stuff(15-(6*2-1), '*');
  // std::cout << stuff * 11 << std::endl;
  Kata Tower;
  std::vector<std::string> built = Tower.towerBuilder(3);
  for(std::string x : built) {
    std::cout << x << std::endl;
  }
  return 0;
}

// other peoples solutions
class Kata2
{
public:
    std::vector<std::string> towerBuilder(int nFloors)
    {
      std::vector<std::string> ret;
      for(int i=0; i<nFloors ; i++)
      {
        ret.push_back(std::string(nFloors-i-1,' ') + 
                      std::string((i*2)+1,'*') +
                      std::string(nFloors-i-1,' '));
      }
      return ret;
    }
};

class Kata
{
public:
    std::vector<std::string> towerBuilder(size_t floor_count)
    {
        assert(floor_count >= 1);
        
        // Calculate width of floors and the center index
        const size_t floor_width = 2 * floor_count - 1;
        const size_t center_index = floor_count - 1;
        
        // Construct with width, so the exact amount of space is immediately reserved
        auto floor_template = std::string(floor_width, ' ');
        
        std::vector<std::string> floors{};
        
        // Kids, remember to reserve the expected amount in vectors, this will greatly speed up your programs!
        floors.reserve(floor_count);
        
        for (size_t it{0}; it != floor_count; ++it) {
        
            // With assert we can test for coding (!) problems.
            assert(center_index - it >= 0);
            assert(center_index + it < floor_template.size());
            
            // Every floor we spread the asterisks further around
            floor_template[center_index - it] = '*';
            floor_template[center_index + it] = '*';
            
            // When pushing back the string it is copied
            floors.push_back(floor_template);
        }
        
        return floors;
    }
};
