#include <iostream>
#include <string>

using std::cout;

// swapping by references

void swap(int &a, int &b)
{
  int temp = a;
  a = b;
  b = temp;

  cout << "a: " << a << "\tb: " << b << "\n";
}

// overloading swap
void swap(std::string a, std::string b) 
{
  std::string temp = a;
  a = b;
  b = temp;

  cout << "a: " << a << "\tb: " << b << "\n";
}

// FIXME: it will throw ambigus error
// void swap(int y, int x)
// {

// }

int main() //main func
{
  int a = 10;
  int b = 20;

  swap(a, b);

  cout << "a: " << a << "\tb: " << b << "\n";
  return 0;
}
