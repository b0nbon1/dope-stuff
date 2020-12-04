#include <iostream>
#include <climits>

using std::cout;

int main() //main func
{
    short a;
    int b;
    long c;
    long long d;
    // short <= int <= long <= long long
    unsigned short e;
    unsigned int f;
    unsigned long g;
    unsigned long long h;
    cout << SHRT_MAX << std::endl;
    cout << USHRT_MAX << std::endl;
    cout << SHRT_MIN << std::endl;
    cout << INT_MAX << std::endl;
    cout << LONG_MAX << std::endl;
    cout << LLONG_MAX << std::endl;
    
    return 0;
}
