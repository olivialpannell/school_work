// Olivia Pannell
// CPCS 121-23
// Program 5

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

struct Employee
{
    string name;
    int years;
    double salary;
};
const int SIZE = 5;
Employee getdata();
void output(Employee employee[], int dsize);
char getchoice();

int main()
{
    int dsize = 0;
    char repeat = 'N';
    Employee employee[SIZE];
    
    do
    {
        employee[dsize] = getdata();
        cout << endl;
        
        if (dsize < 4)
            repeat = getchoice();
        
        dsize++;
    } while (repeat == 'Y' && dsize < 5);
    
    output(employee, dsize);
    
    
    return 0;
}

//gets values
Employee getdata()
{
    Employee e;
    
    cout << "Enter employee name: ";
    getline(cin, e.name);
    
    cout << "Enter years of service: ";
    cin >> e.years;
    
    while (e.years < 0)
    {
        cout << "Invaild input, number must be positive. Try again: ";
        cin >> e.years;
    }
    
    cout << "Enter Salary: ";
    cin >> e.salary;
    
    while (e.salary < 0)
    {
        cout << "Invaild input, number must be positive. Try again: ";
        cin >> e.salary;
    }
    
    return e;
}

//outputs values and averages
void output(Employee employee[], int count)
{
    double avgYear = 0,
    avgSal = 0;
    
    cout << setw(20) << left << "Name" << setw(5) << right
    << "Years" << setw(12) << right << "Salary\n";
    
    for (int i = 0; i < count; i++)
    {
        cout << setw(20) << left << employee[i].name << setw(5) << right
        << employee[i].years << setw(12) << right << setprecision(2) << fixed
        << employee[i].salary << endl;
        
        avgYear = employee[i].years + avgYear;
        avgSal = employee[i].salary + avgSal;
    }
    
    avgYear = avgYear / count;
    avgSal = avgSal / count;
    
    cout << setw(20) << left << "Average" << setw(5) << right
    << setprecision(1) << fixed << avgYear << setw(12) << right
    << setprecision(2) << avgSal << endl;
}

// asks user if they want to run the program again
char getchoice()
{
    char r;
    
    cout << "Enter another employee? (Y/N): ";
    cin >> r;
    cout << endl;
    cin.ignore(100, '\n');
    
    while (r != 'Y' && r != 'N' && r != 'y' && r != 'n')
    {
        cout << "Please enter Y for yes or N for no: ";
        cin >> r;
        cout << endl;
        cin.ignore(100, '\n');
    }
    return toupper(r);
}

