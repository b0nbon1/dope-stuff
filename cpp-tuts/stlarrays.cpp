#include <iostream>
#include <array>

using std::cout;

void print_array(std::array<int, 20> data) {
    for(int i = 0; i < data.size(); i++) {
        cout << data[i] << "\t";
    }
}

int main()
{
    std::array<int, 20> data = {1, 2, 3};
    print_array(data);
    return 0;
}
