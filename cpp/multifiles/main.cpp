#include <iostream>
#include "header.hpp"

// few notes to take
/*
  you can compile your code using g++ directly ie g++ main.cpp file.cpp

  or

  generate a compiled c++ with g++ ie g++ -c main.cpp file.cpp 
  and then run the compile with g++ to produce execuatable ie g++ file.o  main.o
*/

int main()
{
  Rectangle rectangle;
  rectangle.length = 10;
  rectangle.width = 20;
  std::cout << area(rectangle.length, rectangle.width) << std::endl;

  std::cout << area(rectangle.length) << std::endl;

  std::cout << area(rectangle) << std::endl;
}
