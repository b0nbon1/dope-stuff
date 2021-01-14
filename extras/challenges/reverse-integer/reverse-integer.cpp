#include <iostream>
#include <limits.h>

class Solution
{
public:
  int reverse(int x)
  {
    /*
        123 % 10 = 3
        3
        120/10
        12 % 10 = 2
        3*10 + 2 = 32
        10/10 = 1
        1 % 10 = 1
        32*10 + 1 = 321

      */
    int reverse = 0;
    int remainder = 0;
    int state = 1;

    if (x < 0)
    {
      state = -1;
      if (x < -1 * INT_MAX)
        return 0;
      x = x * -1;
    }

      while (x > 0)
      {
        remainder = x % 10;
        if (INT_MAX / 10 < (reverse))
        {
          reverse = 0;
          break;
        }
        reverse = (reverse * 10) + remainder;

        x = x / 10;
      }

    return reverse * state;
  }
};

int main()
{
  Solution sol;

  std::cout << sol.reverse(-83648) << std::endl;

  return 0;
}
