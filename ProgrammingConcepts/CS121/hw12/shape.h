//  Olivia Pannell
//  shape.h
//  Program 12
//  Wednesday Lab

#ifndef shape_h
#define shape_h
#include <iostream>
#include <string>
using namespace std;

class Shape
{
private:
    int x, y;
    string name;
public:
    Shape();
    Shape(int, int, string);
    void setLocation(int, int);
    void print();
};


#endif /* shape_h */
