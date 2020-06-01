#include <iostream>
#include <string>

using std::cout;

int main() //main func
{
    int age = 13;
    std::string bon = "17";

    if(age == 12)
    {
        cout << " you're not old enough \n";
        return -1;
    }
    else if(age < 19) {
        cout << "You're almost 19  \n";
    }
    else
    {
        cout << "False \n";
    }
    cout << "Always";

    switch(age)
    {
        case 13:
            cout << "Your age is 13. Wow \n";
            break;
        case 14:
           cout << "Your age is 14. Wow \n";
        default:
            cout << "Catch all \n";
    }

    // use enums also for switches

    // conditional operator
    int answer = 12;
    int guess = 13;

    guess == answer ? cout << "right guess \n" : cout << "wrong guess \n";
}
