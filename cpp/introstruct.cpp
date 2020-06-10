#include <iostream>

// structs with overloads

struct Rectangle
{
  double width;
  double length;
};

double area(double length, double width)
{
  return length * width;
}

double area(double length)
{
  return length * length;
}

double area(Rectangle rectangle)
{
  return rectangle.width * rectangle.length;
}

int main()
{
  Rectangle rectangle;
  rectangle.length = 10;
  rectangle.width = 20;
  std::cout << area(rectangle.length, rectangle.width) << std::endl;

  std::cout << area(rectangle.length) << std::endl;

  std::cout << area(rectangle) << std::endl;
}