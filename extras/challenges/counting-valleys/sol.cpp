#include <bits/stdc++.h>

using namespace std;

int countingValleys(int steps, string path) {
  int level = 0;
  int valleys = 0;
  for(char& c : path) {
    if(c == 'D') {
      --level;
    } else if (c == 'U') {
        ++level;
    if (level == 0) {
      ++valleys;
    }
    }

  }
  return valleys;
}

int main()
{
  int c = countingValleys(8, "UDDDUDUU");
  cout << c << endl;
}