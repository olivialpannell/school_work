// Olivia Pannell
// CPSC 121-23
// Program 10

#include <iostream>
#include <string>
#include "number.h"
using namespace std;


ostream & operator<< (ostream & out, const Number & n)
{
    out << n.value;
    return out;
}
istream & operator>> (istream & in, Number & n)
{
    int a;
    in >> a;
    n.setFunction(a);
    return in;
}
Number::Number()
{
    value = 0;
}
Number::Number(int n)
{
    setFunction(n);
}
Number::Number(const Number & s)
{
    cout << "Running copy constructor" << endl;
    value = s.value;
}
void Number::setFunction(int n)
{
    if(n>=0 && n<=999)
        value = n;
    else
        exit(1);
    
}
int Number::getFunction()
{
    return value;
    
}
void Number::print()
{
    string one[] = {"","one","two","three","four","five","six","seven","eight","nine", "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"};
    string two[] = {"", "ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"};
    
    if(value >= 100)
    {
        cout << one[value / 100] << " hundred ";
        if (((value % 100) / 10) != 0)
            cout << "and " << two[(value % 100) / 10] << " ";
        if (((value % 100) % 10) != 0)
            cout << one[(value % 100) % 10];
    }
    else if (value < 100 && value > 19)
    {
        cout << two[value /10] << " " << one[value % 10];
    }
    else
        cout << one[value];
    
}
Number Number:: operator+(const Number & op2) const
{
    Number temp;
    temp.value = value + op2.value;
    return temp;
}
Number Number:: operator-(const Number & op2) const
{
    Number temp;
    temp.value = value - op2.value;
    return temp;
    
}
bool Number:: operator>(const Number & op2) const
{
   if (value > op2.value)
       return true;
    else
        return false;
}
bool Number::operator<=(const Number & op2) const
{
    if (value <= op2.value)
        return true;
    else
        return false;
}
Number Number::operator++()
{
    value++;
    return *this;
}
Number Number:: operator++(int)
{
    Number other = *this;
    value++;
    return other;
}
