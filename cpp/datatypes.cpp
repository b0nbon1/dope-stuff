#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <limits>

// hungarian notation =>> the underscore thingie
int g_iRandom = 0;

const double PI = 3.14159;

int main() {
  bool baMarried = false;
  char chMyGrade = 'A';
  unsigned short int u16Age = 21;
  short int siWeight = 180;
  int nDays = 7;
  long lBigNum = 11000000;
  float fPi = 3.14159;
  double dbBigFloat = 1.111111111;
  long double ldPi = 3.14159;
  auto whatWillIBe = true;

  std::cout << "Min bool" <<
    std::numeric_limits<long>::max() << "\n";
  
  std::cout << "int size " << sizeof(int) << "\n";

  // check lost precision
  float fBigFloat = 1.1111111111;
  float fBigFloat2 = 1.1111111111;
  float fFloatSum = fBigFloat2 + fBigFloat;

  printf("fFloatSum Precision : %.10f\n", fFloatSum);

  // Task: convert string to double
  std::string sMiles;
  double dMiles, dKilometers;
  std::cout << "Enter Miles : ";
  getline(std::cin, sMiles);
  dMiles = std::stod(sMiles);
  dKilometers = dMiles * 1.60934;
  printf("%.1f miles equals %.4f kilometers\n", dMiles, dKilometers);

  // convert string to int
  int nInt = std::stoi(sMiles);

  return 0;

}