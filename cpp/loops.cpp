#include <iostream>
#include <string>

using std::cout;
using std::cin;

int main()
{
    // int fact = 10;
    // int factorial = fact;
    // for (int i = factorial; i > 1; i--) {
    //     factorial = factorial * i;
    // }
    // cout << "factorial of " << fact << ": " << factorial << std::endl;
    // int fact = 30;
    // int factorial = 1;
    // while(fact > 1) {
    //     factorial *= fact;
    //     fact--;
    // }
    // cout << "factorial of " << fact << ": " << factorial << std::endl;
    std::string password = "hellotacos123";
    std::string guess;
    do {
        cout << "Guess the password: ";
        cin >> guess;
    } while(guess != password);

    // break statements
    // continue statements
}
