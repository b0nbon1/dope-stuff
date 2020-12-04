#include <iostream>
#include <limits>

using std::cout;

void print_array (int array[], int size) {
    cout << size << std::endl;

    for (int i=0; i < size; i++) {
        cout << array[i] << std::endl;
    }
}

int main()
{
    int guesses[] = {13, 24, 40, 56, 78};
    cout << sizeof(guesses) << std::endl;
    int size = sizeof(guesses) / sizeof(int);
    print_array(guesses, size);

    // int guesses[20];
    // int num_elements = 5;
    // int size = sizeof(datas) / sizeof(datas[0]);
    // for (int i=0; i < num_elements; i++) {
    //     cout << guesses[i] << std::endl;
    // }
    // cout << "Hello world \n";
    // clear the cin
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    return 0;
}
