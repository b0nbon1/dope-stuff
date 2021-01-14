#include <bits/stdc++.h>

using namespace std;

int romanToInt(string s) {
  int sum = 0;
  for (int i = 0; i < s.length(); i++) {
    if(s[i] == 'M') {
      sum += 1000;
      continue;
    } 
    if(s[i] == 'D') {
      sum += 500;
      continue;
    } 
    if(s[i] == 'L') {
      sum += 50;
      continue;
    } 
    if(s[i] == 'C' && s[i+1] == 'M') {
      sum += 900;
      i+=1;
      continue;
    } 
    if(s[i] == 'C' && s[i+1] == 'D') {
      sum += 400;
      i+=1;
      continue;
    } 
    if(s[i] == 'C') {
      sum += 100;
      continue;
    } 
    if(s[i] == 'X' && s[i+1] == 'C') {
      sum += 90;
      i+=1;
      continue;
    } 
    if(s[i] == 'X' && s[i+1] == 'L') {
      sum += 40;
      i+=1;
      continue;
    } 
    if(s[i] == 'X') {
      sum += 10;
      continue;
    } 
    if(s[i] == 'I' && s[i+1] == 'X') {
      sum += 9;
      i+=1;
      continue;
    } 
    if(s[i] == 'I' && s[i+1] == 'V') {
      sum += 4;
      i+=2;
      continue;
    }
    if(s[i] == 'V') {
      sum += 5;
      continue;
    } 
    if(s[i] == 'I') {
      sum += 1;
      continue;
    }
  }
  return sum;
}

int main() {
  cout << romanToInt("MCMXCIV") << endl;
  return 0;
}