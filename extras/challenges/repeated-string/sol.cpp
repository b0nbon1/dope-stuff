#include <bits/stdc++.h>

using namespace std;

long repeatedString(string s, long n) {
  if (s.length() == 1 and s == "a") {
    return n;
  }
  long A = 0;
  for(char& c : s) {
    if(c == 'a') {
       A++;
    }
  }

  long len = n/s.length();
  long rem = n % s.length();
  long allA = len * A;
  for(int i = 0; i < rem; i++) {
    if(s[i] == 'a') {
      allA++;
    }
  }

  return allA;
}

int main()
{
  repeatedString("aba", 10);
  return 0;
}