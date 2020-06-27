//  Olivia Pannell
//  circle.cpp
//  Program 12
//  Wednesday Lab

#include <iostream>
#include <string>
#include <iomanip>
#include <math.h>
#include "shape.h"
#include "circle.h"

//store radius as one
Circle::Circle():Shape(0,0,"Circle")
{
    radius = 1.0;
}
// sends the radius parameter to setRadius
Circle::Circle(int temp1, int temp2, double r):Shape(temp1,temp2,"Circle")
{
    setRadius (r);
}
// checks to make sure radius is greater than 0
void Circle::setRadius(double r)
{
    if(r >0)
        radius = r;
    else
        radius = 1.0;
}
// calculates area
double Circle::calculateArea()
{
    cout << fixed << setprecision(2);
    double area;
    const double PI = 3.14;
    
    area = PI *(pow(radius,2));
    return area;
}
// prints and calls to shapes print function
void Circle::print()
{
    cout << fixed << setprecision(1);
    Shape::print();
    cout << "with a radius of " << radius;
    
}
