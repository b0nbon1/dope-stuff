#include <iostream>
#include <climits>

using std::cout;

int main() //main func
{
    char x = 'A';
    // check ASCII table
    char d = 122;
    // go beyond 128
    unsigned char e = 129;

    // common escape sequences
    cout << "\t";
     cout << "\n";
      cout << "\a";
       cout << "\b";
        cout << "\t";
         cout << "\0";
          cout << "\"";
           cout << "\'";
            cout << "\\";
    
}
