#include <iostream>
#include <fstream>
#include <vector>

using std::cout;
using std::cin;

int main()
{
   std::ifstream file ("writing.txt");

   // check file exists
    if(file.is_open()) {
        std::cout << "success n00b \n";
    }

    std::vector<std::string> names;

    std::string input;
    while(file >> input) {
        names.push_back(input);
    }

    for(std::string name : names) {
        cout << name << std::endl;
    }

    get first char
    char temp = file.get();
    std::cout << temp << "\n";
    std::string line;
    getline(file, line);
    cout << line << "\n";

    return 0;
}

