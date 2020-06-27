// Olivia Pannell
// Wednesday Lab
// Program 13
// rectangle.cpp

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
#include "rectangle.h"

//Rectangle default constructor
Rectangle::Rectangle() :Shape("Rectangle", 0, 0)
{
    width = 1.0;
    height = 1.0;
}

//construct that receives width, height, x and y locations
Rectangle::Rectangle(double w, double h, int x, int y) : Shape("rectangle", x, y)
{
    setWidth(w);
    setHeight(h);
}

//sets width as a double
double Rectangle::setWidth(double w)
{
    if (w > 0)
        width = w;
    else
        width = 1.0;

    return width;
}

//sets height as a double, if not already
double Rectangle::setHeight(double h)
{
    if (h > 0)
        height = h;
    else
        height = 1.0;
    
    return height;
}

// print function and calls for shape print function
void Rectangle::print()
{
    Shape::print();
    cout << " with a width of " << width;
    cout << " and a height of " << height;
    cout << " has an area of " << fixed << setprecision(2);
    cout << calcArea() << endl;
}

//calculates the area of a rectangle
double Rectangle::calcArea()
{
    double area;
    area = width * height;
    
    return area;
}
