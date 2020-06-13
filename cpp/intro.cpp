#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

// TODO: pass arguements after ./a.out call
int main(int argc, char** argv) {
  std::cout << "Hello world" << std::endl;

  if(argc != 1) {
    std::cout << "you have entered " << argc <<
    " arguements \n";
  }

  for(int i = 0; i < argc; ++i) {
    std::cout << argv[i] << "\n";
  }

  return 0;
}