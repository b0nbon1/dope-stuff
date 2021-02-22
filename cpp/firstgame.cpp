#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <fstream>

using std::cout;
using std::cin;
using std::vector;

void save_score(int guess_count) {
    // print_array(guesses, guess_count);
    // TODO:look up how to use ofstream to read and write files
    std::ifstream input("bestscore.txt");
    if(!input.is_open()) {
        cout << "Unable to read file\n";
        return;
    }

    int best_score;
    input >> best_score;

    std::ofstream output("bestscore.txt");
    if(!output.is_open()) {
        cout << "Unable to read file\n";
        return;
    }
    if(guess_count < best_score) {
        output << guess_count;
    } else {
        output << best_score;
    }
}

void print_array(int array[], int count)
{
    for(int i = 0; i < count; i++) {
        cout << array[i] << "\t";
    }

    cout << std::endl;
}

void print_vector(vector<int> vector)
{
    for(int i = 0; i < vector.size(); i++) {
        cout << vector[i] << "\t";
    }

    cout << std::endl;
}

void play_game ()
{
    // int guesses[250];
    vector<int> guesses;
    // int guess_count = 0;
    int count = 0;

    int random = rand() % 251;
    cout << random << std::endl;
    cout << "Guess a number: ";

    while(true) {
        int guess;
        cin >> guess;
        count++;

        // guesses[guess_count++] = guess;
        guesses.push_back(guess);
        if (guess == random) {
            cout << "You win \n";
            break;
        } else if(guess < random) {
            cout << "Too low \n";
        } else {
            cout << "Too high \n";
        }
    }
    save_score(count);
    print_vector(guesses);
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
