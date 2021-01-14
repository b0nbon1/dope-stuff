#include <iostream>
#include <limits.h>

bool isPalindrome(int x)
{
  int num = x;
  if (x < 0)
  {
    return false;
  }

  int reverse = 0;
  int remainder = 0;
  bool overflow = false;
  while (x > 0)
  {
    remainder = x % 10;
    if (INT_MAX / 10 < reverse)
    {
      overflow = true;
      break;
    }
    reverse = (reverse * 10) + remainder;

    x = x / 10;
  }

  if(overflow) {
    return false;
  }
  return reverse == num;
}

int main()
{
  bool pal = isPalindrome(121);
  return 0;
}