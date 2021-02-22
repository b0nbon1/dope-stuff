#include <iostream>

using std::cout;

int main()
{
    int a = 5 + 2;
    int b = 5 - 2;
    int c = 5 * 2;
    int d = 5 / 2; // divisor
    double e = 5.0 / 2; // divosor
    int f = 10 % 4; // modulus

    // precedence BODMAS
    double g = 10 + (4.0 / 3);

    // associativity left to right
    double h = (10 * 4) * 3;
    // right to left
    int i = 10;
    cout << "Hello world \n";
}
