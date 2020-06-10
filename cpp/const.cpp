#include <iostream>
#include <string>

using std::cout;
// global consts
#define X 90

void do_something(int array[]) {

}

void print_array(const int data[], int size)
{
    for (int i = 0; i < size; i++)
    {
        // data[i]++;
        cout << data[i] << "\t";
    }
    cout << "\n";
    // FIXME: will throw error
    // do_something(data);
}

int main() //main func
{
    const int x = 5;
    enum { y= 100 };
    // cout << y;
    auto f = 5U;
    auto c = "  ";
    c = " hold up hold up hold up";
    int data [] = {1, 2, 3};
    print_array(data, 3);
    cout << data[0] << std::endl;
}
