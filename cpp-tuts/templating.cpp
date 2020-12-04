// function templates
#include <iostream>
#include <string>

using std::cout;

template <typename T>
void swap(T &a, T &b)
{
  T temp = a;
  a = b;
  b = temp;

  cout << "a: " << a << "\tb: " << b << "\n";
}

// overloading templates
template<typename T>
void swap(T a[], T b[], int size)
{
  for(int i = 0; i < size; i++) 
  {
    T temp = a[i];
    a[i] = b[i];
    b[i] = temp;
  }
}

int main()
{
  int a = 10;
  int b = 20;

  swap(a, b);

  cout << "a: " << a << "\tb: " << b << "\n";

  std::string lastname = "Bundi";
  std::string firstname = "Bonvic";

  swap(lastname, firstname);

  cout << "last: " << lastname << "\tfirst: " << firstname << "\n";

  int nines[] = {9,9,9,9,9};
  int ones[] = {1,1,1,1,1};

  for (int i = 0; i < 5; i++)
  {
    std::cout << nines[i] << " " << ones[i] << "\t";
  }

  std::cout << "\n\n";

  swap(nines, ones, 5);

  for (int i = 0; i < 5; i++)
  {
    std::cout << nines[i] << " " << ones[i] << "\t";
  }

  return 0;
}
