#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <cmath>

int sockMerchant(int n, std::vector<int> ar) {
  std::unordered_map<int, int> numberFreq;
   for (int i = 0; i < n; i++) {
     numberFreq[ar[i]]++;
   }
   int sum = 0;
   std::unordered_map<int, int>:: iterator p; 
    for (p = numberFreq.begin(); p != numberFreq.end(); p++) {
      sum += p->second/2;
      std::cout << "(" << p->first << ", " << p->second << ")\n";
    }
  return sum;
}


int main()
{
  int pairs = sockMerchant(9, {10,20,20,10,10,30,50,10,20});
  std::cout << pairs << std::endl;
}