#include <iostream>
#include <cmath> 

using std::cout;
using std::cin;



double power(double base, int exponent) //main func
{
    double result = 1;

    for (int i = 0; i < exponent; i++)
    {
        result = result * base;
    }

    return result;
}

void print_pow(double base, int exponent) 
{
    double myPower = power(base, exponent);
    cout << base << " raised to power " << exponent << " is " << myPower << ". \n";
}

int main() //main func
{
    print_pow(10, 10);
    return 0;
}
