// Olivia Pannell
// CPCS 121-23
// Program 3

#include <iostream>
using namespace std;
int menu();
int getSize();
char repeatChoice();
void leftTop(int&);
void rightTop(int&);
void leftBottom(int&);
void rightBottom(int&);


int main ()
{
    int choice, size;
    char repeat;
    do
    {
        choice = menu();
        size = getSize();
    
        if (choice == 1)
            leftTop(size);
        else if (choice == 2)
            leftBottom(size);
        else if (choice == 3)
            rightTop(size);
        else if (choice == 4)
            rightBottom(size);
        
        repeat = repeatChoice();
        
    }while (repeat == 'y' || repeat == 'Y');
    
    return 0;

}

int menu()
{
    int ch;
    cout << "Which triangle do you want to draw?" << endl;
    cout << "1 - Left-Top-Big" << endl;
    cout << "2 - Left-Bottom-Big" << endl;
    cout << "3 - Right-Top-Big" << endl;
    cout << "4 - Right-Bottom-Big" << endl;
    cin >> ch;
    
    while (ch < 1 || ch > 4)
    {
        cout << "Illegal choice. Try again :";
        cin >> ch;
    }
    return ch;
}

int getSize()
{
    int a;
    cout << "Please enter the maximum size (1-10):";
    cin >> a;
    
    while (a < 1 || a > 10)
    {
        cout << "Size must be in the range 1-10. Please try again: ";
        cin >> a;
    }
    return a;
}

char repeatChoice()
{
    char r;  // r = repeat
    cout << "Draw another? (Y/N): ";
    cin >> r;
    
    while (r != 'Y' && r != 'y' && r != 'N' && r != 'n')
    {
        cout << "Please enter Y for yes or N for no: ";
        cin >> r;
    }

    return r;
}


void leftTop(int& n)
{
    
    for (int i = n; i > 0; i--)
    {
        for (int k = i; k >= 1; k--)
            cout << "*";
        cout << endl;
    }
    
}
void leftBottom(int& n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int k = i; k >= 1; k--)
            cout << "*";
        cout << endl;
    }
}


void rightTop(int& n)
{
    for (int i = n; i > 0; i--)
    {
        for (int b = n-i; b > 0; b--)
            cout << " ";
        for (int k = i; k >= 1; k--)
            cout << "*";
        cout << endl;
    }
}

void rightBottom(int& n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int b = n-i; b > 0; b--)
            cout << " ";
        for (int k = i; k >= 1; k--)
            cout << "*";
        cout << endl;
    }
}
