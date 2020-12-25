#include <iostream>

int main()
{
  std::string name;

  std::cout << "Hello world!, who can I call you?" << std::endl;
  // single word
  std::cin >> name;
  // multiple words
  std::getline(std::cin, name);
  std::cout << "Hello " << name << std::endl;
  return 0;
}
