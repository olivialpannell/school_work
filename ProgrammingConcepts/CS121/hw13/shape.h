// Olivia Pannell
// Wednesday Lab
// Program 13
// shape.h

#include <iostream>
#include <string>
using namespace std;

#ifndef shape_h
#define shape_h

class Shape
{
private:
    int xCoordinate;
    int yCoordinate;
    string shapeType;
public:
    Shape();
    Shape(string shape, int x, int y);
    void setLocation(int xLocation, int yLocation);
    virtual void print();
    virtual double calcArea() = 0;
};

#endif
