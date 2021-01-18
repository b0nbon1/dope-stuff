#include <bits/stdc++.h>

using namespace std;

bool compareLen(const std::string& a, const std::string& b)
{
    return (a.size() < b.size()); 
}

string longestCommonPrefix(vector<string>& strs) {
  if(strs.size() <= 0) {
    return "";
  }
  string prefix = "";
  bool check = false;
  int j=0;
  for (int i=0; i<strs[0].size(); i++) {
    for (int j=0; j<strs.size()-1; j++) {
      if(strs[j][i] != strs[j+1][i]) {
        check = true;
        break;
      }
    }
      if(check) break;
      prefix = prefix + strs[0][i];
  }
  return prefix;
}

int main() {
  vector<string> str = {};
  sort(str.begin(), str.end(), compareLen);
  cout << longestCommonPrefix(str) << std::endl;
  return 0;
}