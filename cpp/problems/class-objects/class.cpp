#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

// Write your Student class here
class Student
{
    size_t mSize;
    int *mArray;

public:
    Student(size_t s = 0)
    {
        mSize = s;
        mArray = new int[mSize];
    }
    void input()
    {
    }
    int calculateTotalScore()
    {
        return 0;
    }
};

int main()
{
    int n; // number of students
    string str;
    cin >> n;
    // Student *s = new Student[n]; // an array of n students

    for (int i = 0; i < n; i++)
    {
        cout << "Please enter your name: \n";
        getline(cin, str);
        cout << "Hello, " << str
             << " welcome to GfG !\n";
    }

    // // calculate kristen's score
    // int kristen_score = s[0].calculateTotalScore();

    // // determine how many students scored higher than kristen
    // int count = 0;
    // for (int i = 1; i < n; i++)
    // {
    //     int total = s[i].calculateTotalScore();
    //     if (total > kristen_score)
    //     {
    //         count++;
    //     }
    // }

    // // print result
    // cout << count;

    return 0;
}
