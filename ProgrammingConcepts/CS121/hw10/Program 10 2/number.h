//  Olivia Pannell
//  Header.h
//  Program 10
//  CPSC 121-23
#ifndef Header_h
#define Header_h

#include <iostream>
#include "number.h"
using namespace std;

class Number
{
    friend ostream & operator<< (ostream &, const Number &);
    friend istream & operator>> (istream &, Number &);
    
private:
    int value;
    
public:
    Number();
    Number(int n);
    Number(const Number & s);
    void setFunction(int n);
    int getFunction();
    void print();
    Number operator+(const Number & op2) const;
    Number operator-(const Number & op2) const;
    bool operator>(const Number & op2) const;
    bool operator<=(const Number & op2) const;
    Number operator++();
    Number operator++(int);
};



#endif /* Header_h */
