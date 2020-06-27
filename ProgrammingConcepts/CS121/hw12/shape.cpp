//  Olivia Pannell
//  shape.cpp
//  Program 12
//  Wednesday Lab

#include <iostream> 
#include <string>
#include "shape.h"
using namespace std;

// sets x and y to be zero and sets the name to be unknown
Shape::Shape()
{
    x = 0;
    y = 0;
    name = "Unknown shape";
}
// sets temp1 and temp2 to private data
Shape::Shape(int temp1, int temp2, string tempS)
{
    x = temp1;
    y = temp2;
    name = tempS;
}
// sets private data fields
void Shape::setLocation(int temp1, int temp2)
{
    x = temp1;
    y = temp2;
}
//prints
void Shape::print()
{
    cout << name << " at (" << x << ", " << y << ")";
}
