#include <iostream>
#include <cmath>

using std::cout;

int main()
{
    // square root
    // inf for infinity
    // nan not a number
    sqrt(25);
    remainder(10, 3); // retruns remainder
    // 10 % 3.25; // wont work
    remainder(10, 3.25); // will work
    fmod(10, 3.25); // similar to remainder
    fmin(10, 3.25); // return min
    fmax(10, 3.25); // return max
    ceil(3.25); // ceil 4
    floor(3.25); // floor 3
    trunc(3.25); // truncate 3
    floor(-3.25); // floor -4
    trunc(-3.25); // truncate -3
    round(-3.5); // roundoff to 4
    
}
