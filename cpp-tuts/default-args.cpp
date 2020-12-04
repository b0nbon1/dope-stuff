#include <iostream>

using std::cout;

double pow(double base, int pow = 2)
{
  int total = 1;
  for(int i = 0; i < pow; i++)
  {
    total *= base;
  }
  return total;
}

int main() //main func
{
  cout << pow(3)<<"\n";
  return 0;
}
