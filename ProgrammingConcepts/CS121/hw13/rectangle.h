// Olivia Pannell
// Wednesday Lab
// Program 13
// rectangle.h

#include <iostream>
#include <string>
using namespace std;
#include "shape.h"

#ifndef rectangle_h
#define rectangle_h

class Rectangle:public Shape
{
    
private:
    double width;
    double height;
public:
    Rectangle();
    Rectangle(double w, double h, int x, int y);
    double setWidth(double w);
    double setHeight(double h);
    virtual void print();
    virtual double calcArea();
};

#endif
