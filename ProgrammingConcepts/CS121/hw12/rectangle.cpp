//  Olivia Pannell
//  rectangle.cpp
//  Program 12
//  Wednesday Lab

#include <iostream>
#include <string>
#include <iomanip>
#include "shape.h"
#include "rectangle.h"
using namespace std;

// sets width and height to 1
Rectangle::Rectangle():Shape(0,0, "Rectangle")
{
    width = 1.0;
    height = 1.0;
}
// calls width and height functions
Rectangle::Rectangle(int temp1, int temp2, double w, double h):Shape(temp1,temp2,"Rectangle")
{
    setWidth(w);
    setHeight(h);
}
// makes sure width is postive, if not sets to 1.0
void Rectangle::setWidth(double w)
{
    if (w > 0)
        width = w;
    else
        width = 1.0;
}
// makes sure height is postive, if not sets to 1
void Rectangle::setHeight(double h)
{
    if ( h > 0)
        height = h;
    else
        height = 1.0;
}
// calculates the area of a rectangle
double Rectangle::calculateArea()
{
    double area;
    area = width * height;
    return area;
}
// prints and call the shape print function
void Rectangle::print()
{
    cout << fixed << setprecision(1);
    Shape::print();
    cout << " with a height of " << height << " and a width of ";
    cout << fixed << setprecision(2) << width << endl;
}
