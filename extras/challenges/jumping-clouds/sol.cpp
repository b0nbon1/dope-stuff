#include <bits/stdc++.h>

using namespace std;

int jumpingOnClouds(vector<int> c) {
int inc = 0;
  int steps = 0;
  bool skip = true;
  while (inc < c.size())
  {
    if(c[inc] == 1) {
      inc++;
      skip = true;
      continue;
    }
    else if(c.size() == (inc+1)) {
        inc++;
        continue;
    } else if(c[inc] == 0 and c[inc+1] == 0 and c[inc+2] == 0) {
      inc+=2;
      steps++;
      skip = false;
      continue;
    } 
     else if(c[inc] == 0) {
      inc++;
      steps++;
      skip = true;
      continue;
    }
  }
  
  return steps; 

}

int main()
{
  int step = jumpingOnClouds({0, 0, 1, 0, 0, 1, 0});
  cout << step << endl;
}
