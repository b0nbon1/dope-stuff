#include <bits/stdc++.h>
using namespace std;

int sumArr(vector<int> ar)
{
  int sum = 0;
  for (int i = 0; i < ar.size(); i++)
  {
    sum += ar[i];
  }
  return sum;
}

int hourglassSum(vector<vector<int>> arr) {
  vector<int> comb;
  for(int x=0; x<4; x++){
    for(int y=0; y<4; y++){
     vector<int> k = {
       arr[x][y], arr[x][y+1], arr[x][y+2],
                 arr[x+1][y+1],
      arr[x+2][y],arr[x+2][y+1],arr[x+2][y+2]
      };
      for(int i = 0; i < k.size(); i++) {
        cout << k[i] << "\t";
      }
      cout << endl;
      comb.push_back(sumArr(k));
    }
  }

  return *max_element(comb.begin(), comb.end());
}

int main()
{
  vector<vector<int>> rr = {
    {1,1,1,0,0,0},
    {0,1,0,0,0,0},
    {1,1,1,0,0,0},
    {0,0,2,4,4,0},
    {0,0,0,2,0,0},
    {0,0,1,2,4,0}
    };
  cout << "the largest sum is: " << hourglassSum(rr) << endl;
}