//  Olivia Pannell
//  main.cpp
//  Program 10
//

#include <iostream>
#include <string>
#include "number.h"
using namespace std;

int main()
{
    Number one, two(654);
    cout << "Number One(): " << one << endl;
    one.print();
    cout << endl << endl;
    
    cout << "Number Two(654): " << two << endl;
    two.print();
    cout << endl << endl;
    
    cout << "Enter new number for One: ";
    cin >> one;
    one.print();
    cout << endl << endl;

    Number three = one + two;
    cout << "Number three is the sum of # one and # two: " << three << endl;
    three.print();
    cout << endl << endl;
    
    Number four = three - two;
    cout << "Four is the difference of # three and # two: " << four << endl;
    four.print();
    cout << endl << endl;
    
    Number five = two;
    cout << "Five is from # two: " << five << endl;
    five.print();
    cout << endl << endl;
    
    if (five > four)
        cout << "Five is greater than # four." << endl;
    else
        cout << "Four is greater than # five." << endl;
    
    cout << endl;
    if (three <= four)
        cout << " # two is less than or equal to # three." << endl;
    else
        cout << "# two is greater than # three." << endl;
    Number six(12);
    cout << "Increment six(12) while return value: " << six << endl;
    six++.print();
    cout << endl;
    cout << six << endl;
    six.print();
    cout << endl << endl;
    
    Number seven(700);
    cout << "Increment seven(700) ";
    cout << ++seven << endl;
    seven.print();
    
    cout << endl << endl;;

    return 0;
}
