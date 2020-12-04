#include <iostream>

class Position
{
  public:
    int x = 10;
    int y = 20;
    Position operator + (Position pos)
    {
      Position new_pos;
      new_pos.x = x + pos.x;
      new_pos.y = y + pos.y;
      return new_pos;
    }
    bool operator == (Position pos)
    {
      Position new_pos;
      if (new_pos.y == y && new_pos.x == x) return true;
      return false;
    }
};


std::ostream& operator << (std::ostream& output, Position pos)
{
  output << "X: " << pos.x << "\nY: " << pos.y;
  return output;
}

std::istream& operator >> (std::istream& input, Position &pos)
{
  std::cout << "enter X: ";
  input >> pos.x;
  std::cout << "enter Y: ";
  input >> pos.y;
  return input;
}

int main()
{
  Position pos1, pos2;
  pos1.y = 22;
  pos2.y = 31;
  std::cin >> pos2;
  Position pos3 = pos1 + pos2;
  std::cout << pos3.x << " " << pos3.y << std::endl;
  if (pos1 == pos2)
  {
    std::cout << "I love tacos \n";
  }

  std::cout << pos2 << std::endl;
  return 0;
}