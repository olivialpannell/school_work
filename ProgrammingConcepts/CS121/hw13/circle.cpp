// Olivia Pannell
// Wednesday Lab
// Program 13
// circle.cpp

#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
#include "circle.h"

const double PI = 3.14;

//default constructor
Circle::Circle():Shape("Circle", 0, 0)
{
    radius = 1.0;
}

//constructor that receives x, y, and radius values
Circle::Circle(int x, int y, double r):Shape("Circle", x, y)
{
    setRadius(r);
}

//receives a double and sets double as the radius
double Circle::setRadius(double r)
{
    if (r > 0)
        radius = r;
    else
        radius = 1.0;
    return radius;
}

//prints and calls shape print's function
void Circle::print()
{
    Shape::print();
    cout << " with a radius of " << radius
    << " and has an area of " << fixed << setprecision(2)
    << calcArea() << endl;
}

//calculates the area of a circle
double Circle::calcArea()
{
    double area;
    area = PI * pow(radius, 2);
    return area;
}
