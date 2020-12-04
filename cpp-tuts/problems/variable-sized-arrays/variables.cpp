#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int q;
    int i;
    int d;
    int qr;
    int qi;

    vector<vector<int>> arr;
    vector<int> a;
    vector<int> qa;
    cin >> n;
    cin >> q;

    while (n > 0)
    {
        a.clear();
        cin >> i;
        while (i > 0)
        {
            cin >> d;
            a.push_back(d);
            i--;
        }
        arr.push_back(a);
        n--;
    }

    while(q > 0)
    {
        cin >> qi;
        cin >> qr;
        cout << arr[qi][qr] << endl;
        q--;
    }

    return 0;
}
