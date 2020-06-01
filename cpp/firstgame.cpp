#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using std::cout;
using std::cin;

void play_game () {
    int random = rand() % 251;
    cout << random << std::endl;
    cout << "Guess a number: ";

    while(true) {
        int guess;
        cin >> guess;
        if (guess == random) {
            cout << "You win \n";
            break;
        } else if(guess < random) {
            cout << "Too low \n";
        } else {
            cout << "Too high \n";
        }
    }
}

int main() //main func
{
    srand(time(NULL));
    int choice;
    do {cout << "0. Quit" << std::endl << "1. Play Game \n";
    cin >> choice;

    switch(choice) {
        case 0:
            cout << "Thanks for nothing \n";
            break;
        case 1:
            cout << "yo let's play the game \n";
            play_game();
            break;
        }
    } while (choice != 0);
}
