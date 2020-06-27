//// Olivia Pannell
//// CPSC 121-23
//
//#include <iostream>
//using namespace std;
//
//void get2Char(char&, char&);
//void putInOrder(char&, char&);
//void count(char, char, int&, int&, int&);
//void output(char, char, int, int, int);
//char getChoice();
//
//
//int main ()
//{
//    char repeat, ch1, ch2;
//    int upper, lower, digits;
//    
//    do{
//        get2Char(ch1, ch2);
//        putInOrder(ch1, ch2);
//        count(ch1, ch2, upper, lower, digits);
//        output(ch1, ch2, upper, lower, digits);
//        repeat = getChoice();
//        
//    }while(repeat == 'y' || repeat == 'Y');
//
//    return 0;
//}
//
//// Gets the characters from the user
//void get2Char(char& ch1, char& ch2)
//{
//
//    cout << "Enter two characters: ";
//    cin >> ch1 >> ch2;
//    cin.ignore();
//    cout << endl;
//    
//}
//
//// Puts the characters in order from lower to higher
//void putInOrder(char& ch1, char& ch2)
//{
//    if (ch1 > ch2)
//        swap(ch1, ch2);
//    
//}
//
//// counts how many digits, lowercase, uppercase, there are in
//// between the two characters the user chose
//void count(char ch1, char ch2, int& up, int& low, int& dig)
//{
//    low = 0;
//    up = 0;
//    dig = 0;
//    for (char i = ch1; i <= ch2; i++)
//    {
//        if (islower(i))
//            low++;
//        else if (isupper(i))
//            up++;
//        else if (isdigit(i))
//            dig++;
//            
//    }
//    
//}
//
//// output statement
//void output(char ch1, char ch2, int up, int low, int dig)
//{
//    cout << "Between " << ch1 << " and " << ch2 << " there are " << up << " upper case, ";
//    cout << low << " lower case, and " << dig << " digits." << endl;
//}
//
//// asks user if they want to run the program again
//char getChoice()
//{
//    char r;  // r = repeat
//    cout << "Enter other characters? (Y/N): ";
//    cin >> r;
//    
//    while (r != 'Y' && r != 'y' && r != 'N' && r != 'n')
//    {
//        cout << "Please enter Y for yes or N for no: ";
//        cin >> r;
//    }
//    
//    return r;
//}
