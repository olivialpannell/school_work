// Olivia Pannell
// Wednesday Lab
// Program 13
// shape.cpp

#include <iostream>
#include <string>
using namespace std;
#include "shape.h"

//default constructor
Shape::Shape()
{
    string shapeType = "unknown shape";
    xCoordinate = 0;
    yCoordinate = 0;
}

//constructor that receives shape, x and y values
Shape::Shape(string shape, int x, int y)
{
    shapeType = shape;
    setLocation(x, y);
}

//sets x and y as the location
void Shape::setLocation(int x, int y)
{
    xCoordinate = x;
    yCoordinate = y;
}

// print function
void Shape::print()
{
    cout << shapeType << " at (" << xCoordinate
    << "," << yCoordinate << ")" << endl;
}
