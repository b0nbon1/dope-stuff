#include <math.h>
#include <iostream>
#include <cmath>

long square(long number)
{
  return number * number;
}

long solve(long n){
  long starter = (long)1e9;
  long sq = 1;
  long temp;
  double sqr;
  long sol = -1;

  while(square(sq+1) - square(sq) <= n) {
    std::cout << square(sq) << "\n";

    temp = square(sq);
    sqr = std::sqrt(temp + n);
    if(int(sqr) == sqr)
      {
        sol = temp;
        break;
      }
    sq++;
  }
  return sol;
}

int main() {
  std::cout << solve(290101) << std::endl;
}