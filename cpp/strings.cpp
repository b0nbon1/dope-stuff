#include <iostream>
#include <string>

using std::cout;
using std::cin;

int main()
{
    std::string greeting = "hello";
    greeting += " bon ";
    // cout << greeting + " there there" << std::endl;
    // cout << greeting.length() << std::endl;
    // method === member func

    char name[] = "bon bon"; //c string == array of characters
    // input strings
    // getline(cin, greeting);
    // cout << greeting.size() << std::endl;
    // cout <<  greeting.append(' bruh') << std::endl;
    greeting.insert(5, " interfere ");
    greeting.erase(3, 4);
    greeting.erase(greeting.length() - 1);
    greeting.pop_back();
    // index, length, word
    greeting.replace(0, 4, "replace hell : : :");
    cout << greeting.find(":") << std::endl;;
    greeting.replace(greeting.find("hell"), 4, "****");
    greeting.substr(5,2);
    cout << greeting.find_first_of("r") << std::endl;
    cout << greeting.find_first_of("2") << std::endl; // returns npos which is -1
    cout << greeting << std::endl;
    greeting = "What is up?";
    if (greeting == "What is up?") cout << " Equals" << std::endl;
    if (greeting.compare("What is up?") == 0) cout << " Equals" << std::endl;
}
