//  Program #1.cpp
//  CPCS 121-23
//  Olivia Pannell


#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
    string nameOne,
        nameTwo;
    
    int yearOne,
        yearTwo;
    
    double averageS,
        averageY,
        salaryOne,
        salaryTwo;
    
    
    cout << "Name of employee: ";
    getline (cin, nameOne);
    
    cout << "Years of service: ";
    cin >> yearOne;
    
    cout << "Current salary: ";
    cin >> salaryOne;
    
    cin.ignore();
    
    cout << "Name of employee: ";
    getline (cin, nameTwo);
    
    cout << "Years of service: ";
    cin >> yearTwo;
    
    cout << "Current salary: ";
    cin >> salaryTwo;

    cout << fixed << setprecision(2);
    averageS = (salaryOne + salaryTwo) / 2;
    averageY = (yearOne + yearTwo) / 2.0;
    
    cout << "\nEmployee data\n";

    
    cout << left << setw(20) << "Name";
    cout << right << setw(5) << "Years";
    cout << right << setw(12) << "Salary" << endl;
    
    cout << left << setw(20) << nameOne;
    cout << right << setw(5) << yearOne;
    cout << right << setw(12) << salaryOne << endl;
    
    cout << left << setw(20) << nameTwo;
    cout << right << setw(5) << yearTwo;
    cout << right << setw(12) << salaryTwo << endl;
    
    cout << left << setw(20) << "Average";
    cout << setprecision(1) << right << setw(5) << averageY;
    cout << setprecision(2) << right << setw(12) << averageS << endl;
    
    
    return 0;
}
