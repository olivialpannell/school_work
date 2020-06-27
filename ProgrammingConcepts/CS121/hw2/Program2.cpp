//  Olivia Pannell
//  Program #2
//  CPCS 121-23

#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

int main()
{
    int number,
    tries,
    random,
    roll = 0;
    
    double avg = 0;
    
    do
    {
    cout << "Enter a number between 2 and 12: ";
    cin >> number;
    
    if (number < 2 || number > 12)
        cout << "Invalid number." << endl;
    else
    {
        cout << "How many tries do you want? ";
        cin >> tries;
        
        while(tries <= 0)
        {
            cout << "Invalid input." << endl;
            cout << "How many tries do you want? ";
            cin >> tries;
        }
        
        srand ((int)time (NULL));
        
            
        for (int i=0; i <= tries;)
        {
            random = rand() % 12 + 1;
            roll = roll + 1;
            if (number == random)
            {
                cout << "Found " << number << " on roll " << roll << endl;
                i++;
                avg += roll;
                roll = 0;
            }
        }

        avg = avg / tries;
        cout << "In " << tries << " tries, found " << number << " in an average ";
        cout << "of " << setprecision(1) << fixed << avg << " rolls.\n";

    }
    
    }while(number < 2 || number > 12);
    
    
    return 0;
}
