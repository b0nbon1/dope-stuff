#include <iostream>
#include <float.h>

using std::cout;

int main() //main func
{
    float a;
    double b = 7.7E4; // 7.7E4 7.7 * 10^4
    long double c;

    cout << std::fixed << b << std::endl;
    cout << FLT_DIG << std::endl;
    cout << DBl_DIG << std::endl;
    cout << LDBL_DIG << std::endl;
}
