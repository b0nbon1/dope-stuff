#include <iostream>
#include <string>

using std::cout;
using std::cin;

// throw error when called
void test(int data[]) {
    for(int n : data)
    {
        cout << n << "\t";
    }
}

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
    // std::string password = "hellotacos123";
    // std::string guess;
    // do {
    //     cout << "Guess the password: ";
    //     cin >> guess;
    // } while(guess != password);
    int data[] = {1, 2, 3, 4, 5, 6};
    for(int n : data)
    {
        cout << n << "\t";
    }

    // break statements
    // continue statements
}
