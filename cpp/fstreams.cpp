#include <iostream>
#include <fstream>
#include <vector>

using std::cout;
using std::cin;

int main()
{
    // std::ofstream file;
    // file.open("hello.txt");
    std::string filename;
    cin >> filename;

    std::ofstream file (filename.c_str(), std::ios::app);

    if(file.is_open()) {
        std::cout << "success n00b \n";
    }
    
    // file << "hey";
    std::vector<std::string> names;
    names.push_back("Caleb");
    names.push_back("Bon Bon");
    names.push_back("Amy");
    names.push_back("Susan");

    for (std::string name : names) {
        // writing to files
        file << name << std::endl;
    }

    file.close();
    return 0;
}
